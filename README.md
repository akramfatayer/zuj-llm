# Large Language Models and Query Engineering

**Al-Zaytoonah University of Jordan** · BSc Data Science and Artificial Intelligence
**Instructor:** Dr. Akram Fatayer

> Labs are Jupyter notebooks on open-weight models. They run in the department's GPU lab and on Google Colab, so no paid API is needed.

Course page and interactive modules: https://akramfatayer.github.io/courses/llm

---

## Course Structure

| Week | Topic | Lab |
|------|-------|-----|
| 1 | What LLMs are: next-token prediction, the model landscape | Lab 01: Hello, LLM |
| 2 | Tokenization and embeddings | Lab 02: Tokens and Embeddings |
| 3 | Self-attention and the transformer decoder | Lab 03: Attention from Scratch |
| 4 | Pre-training, scaling and decoding | Lab 04: Decoding |
| 5 | Instruction tuning, LoRA and alignment | Lab 05: Adapting a Model |
| 6 | Prompt engineering I | Lab 06: A Prompt Test Harness |
| 7 | Prompt engineering II: reasoning and decomposition | Lab 07: Reasoning and Prompt Chains |
| 8 | Structured outputs, cost and latency | Lab 08: Structured Outputs |
| 9 | Semantic search and vector databases | Lab 09: Semantic Search |
| 10 | Retrieval-augmented generation | Lab 10: RAG |
| 11 | Tool use, text-to-SQL and agents | Lab 11: Tool-Calling Agents |
| 12 | Evaluating LLM systems | Lab 12: Evaluating LLM Systems |
| 13 | Safety, security and deployment | Lab 13: Red-Teaming |
| 14–15 | Team project studio and demos | — |

## Repo Structure

```
lectures/     — Weekly slides (PDF)
labs/
  lab-01-hello-llm/          — Next-token probabilities, the generation loop, chat templates, failure log
  lab-02-tokens-embeddings/  — Five tokenizers, fertility and cost in Arabic and English, embeddings; mini-assignment 1 brief
project/      — Team project brief and rubric (published in week 3)
setup/        — Lab PC setup: requirements.txt, prefetch_models.py (downloads every model), check_lab_pc.py
```

## Running the labs

- **GPU lab:** models are cached on the machines (lab supervisors: run `setup/prefetch_models.py`, then `setup/check_lab_pc.py`). Set `LAB_MODEL`, `LAB_SERVER` and `LAB_SERVER_MODEL` to point the notebooks at the local model server.
- **Colab:** open a notebook with its *Open in Colab* badge and choose a T4 GPU runtime.
