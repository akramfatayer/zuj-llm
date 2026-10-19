"""Checks that a lab PC is ready for the week 1–2 labs, with no internet access.

    python check_lab_pc.py

Prints one line per check and ends with READY or NOT READY. Takes 1–2 minutes
(it loads the lab model once). Run it after prefetch_models.py.
"""
import os
import shutil
import sys

os.environ["HF_HUB_OFFLINE"] = "1"  # prove everything is cached: no downloads allowed

problems = []


def ok(msg):
    print(f"  OK    {msg}")


def bad(msg):
    print(f"  FAIL  {msg}")
    problems.append(msg)


def warn(msg):
    print(f"  NOTE  {msg}")


print("Python and packages")
if sys.version_info >= (3, 10):
    ok(f"Python {sys.version.split()[0]}")
else:
    bad(f"Python {sys.version.split()[0]}: 3.10 or newer is needed")
try:
    import torch
    import transformers

    transformers.logging.set_verbosity_error()  # hide library warnings; this script reports what matters

    ok(f"torch {torch.__version__}, transformers {transformers.__version__}")
    for pkg in ["accelerate", "sentencepiece", "openai", "requests", "pandas", "matplotlib", "ipykernel"]:
        __import__(pkg)
    ok("accelerate, sentencepiece, openai, requests, pandas, matplotlib, ipykernel")
except ImportError as e:
    bad(f"missing package: {e.name} (pip install -r requirements.txt)")
    print("\nNOT READY")
    sys.exit(1)

print("\nGPU")
if torch.cuda.is_available():
    props = torch.cuda.get_device_properties(0)
    gb = props.total_memory / 1024**3
    ok(f"{props.name}, {gb:.1f} GB memory, CUDA {torch.version.cuda}")
    if gb < 6:
        warn("under 6 GB: Lab 01 still runs, but later labs need a larger GPU or the shared server")
else:
    bad("no CUDA GPU visible to PyTorch (check the driver, and that torch is the CUDA build, not +cpu)")

print("\nDisk and cache")
cache = os.environ.get("HF_HOME", os.path.join(os.path.expanduser("~"), ".cache", "huggingface"))
ok(f"HF_HOME = {cache}")
free_gb = shutil.disk_usage(os.path.dirname(os.path.abspath(cache)) or ".").free / 1024**3
(ok if free_gb >= 20 else warn)(f"{free_gb:.0f} GB free on the cache drive (20 GB or more recommended for later labs)")

print("\nTokenizers (Lab 02, offline)")
from transformers import AutoModel, AutoModelForCausalLM, AutoTokenizer

for repo in ["openai-community/gpt2", "Qwen/Qwen2.5-1.5B-Instruct", "google-bert/bert-base-multilingual-cased",
             "FacebookAI/xlm-roberta-base", "aubmindlab/bert-base-arabertv02"]:
    try:
        n = len(AutoTokenizer.from_pretrained(repo)("يسافر الطلاب من إربد إلى العقبة.", add_special_tokens=False).input_ids)
        ok(f"{repo} ({n} tokens for the Arabic test sentence)")
    except Exception as e:
        bad(f"{repo}: {type(e).__name__}")
for repo in ["google/mt5-small", "facebook/nllb-200-distilled-600M", "CAMeL-Lab/bert-base-arabic-camelbert-mix"]:
    try:
        AutoTokenizer.from_pretrained(repo)
        ok(f"{repo} (mini-assignment 1)")
    except Exception:
        warn(f"{repo} not cached: optional, students can download it at home for mini-assignment 1")

print("\nEmbedding model (Lab 02, Part C)")
try:
    AutoModel.from_pretrained("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    ok("paraphrase-multilingual-MiniLM-L12-v2 loads")
except Exception as e:
    bad(f"embedding model: {type(e).__name__}")

print("\nLab model (Lab 01)")
model_id = os.environ.get("LAB_MODEL", "Qwen/Qwen2.5-1.5B-Instruct")
try:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    tok = AutoTokenizer.from_pretrained(model_id)
    try:
        model = AutoModelForCausalLM.from_pretrained(model_id, dtype=dtype)
    except TypeError:
        model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=dtype)
    model = model.to(device).eval()
    with torch.no_grad():
        logits = model(**tok("The capital of Jordan is", return_tensors="pt").to(device)).logits[0, -1]
    top = tok.decode([int(logits.argmax())])
    ok(f"{model_id} on {device}: next token after 'The capital of Jordan is' = {top!r}")
except Exception as e:
    bad(f"{model_id}: {type(e).__name__}: {e}")

print("\nLocal model server (optional)")
server = os.environ.get("LAB_SERVER", "http://localhost:11434/v1")
try:
    import requests

    r = requests.get(f"{server}/models", timeout=2)
    names = [m.get("id") for m in r.json().get("data", [])] if r.ok else []
    ok(f"server at {server}: {', '.join(names) or 'no models'}")
except Exception:
    warn(f"no server at {server}: fine, the notebooks then run the model directly")

print("\nREADY" if not problems else f"\nNOT READY: {len(problems)} problem(s) above")
sys.exit(1 if problems else 0)
