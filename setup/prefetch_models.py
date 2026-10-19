"""Downloads every model and tokenizer the week 1–2 labs (and mini-assignment 1) use.

Run once per PC, or once on a shared drive that all PCs point HF_HOME at:

    set HF_HOME=D:\\hf-cache          (Windows; Linux: export HF_HOME=/opt/hf-cache)
    python prefetch_models.py

Afterwards the labs run with no internet (set HF_HUB_OFFLINE=1). Safe to re-run:
files already downloaded are skipped.
"""
import os
import sys

from huggingface_hub import snapshot_download
from transformers import AutoTokenizer

# Full models (weights + tokenizer): (Hugging Face id, used in)
MODELS = [
    ("Qwen/Qwen2.5-1.5B-Instruct", "Lab 01 (all parts), Lab 02 tokenizer"),
    ("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", "Lab 02 Part C (embeddings)"),
]
# Tokenizers only (a few MB each): (Hugging Face id, used in)
TOKENIZERS = [
    ("openai-community/gpt2", "Lab 02"),
    ("google-bert/bert-base-multilingual-cased", "Lab 02"),
    ("FacebookAI/xlm-roberta-base", "Lab 02"),
    ("aubmindlab/bert-base-arabertv02", "Lab 02"),
    ("google/mt5-small", "Mini-assignment 1 (optional extra tokenizer)"),
    ("facebook/nllb-200-distilled-600M", "Mini-assignment 1 (optional extra tokenizer)"),
    ("CAMeL-Lab/bert-base-arabic-camelbert-mix", "Mini-assignment 1 (optional extra tokenizer)"),
]
# Model files the labs never load; skipping them saves several GB
SKIP = ["*.onnx", "onnx/*", "openvino/*", "*.h5", "*.msgpack", "*.ot", "tf_model*", "flax_model*", "rust_model*", "pytorch_model*.bin"]


def main():
    cache = os.environ.get("HF_HOME", os.path.join(os.path.expanduser("~"), ".cache", "huggingface"))
    print(f"Cache folder: {cache}\n")
    failed = []
    for repo, use in MODELS:
        print(f"[model]     {repo}  ({use})")
        try:
            snapshot_download(repo, ignore_patterns=SKIP)
        except Exception as e:  # keep going, report at the end
            failed.append((repo, e))
    for repo, use in TOKENIZERS:
        print(f"[tokenizer] {repo}  ({use})")
        try:
            AutoTokenizer.from_pretrained(repo)
        except Exception as e:
            failed.append((repo, e))
    print()
    if failed:
        for repo, e in failed:
            print(f"FAILED  {repo}: {e}")
        sys.exit(1)
    print("All downloads complete. Now run:  python check_lab_pc.py")


if __name__ == "__main__":
    main()
