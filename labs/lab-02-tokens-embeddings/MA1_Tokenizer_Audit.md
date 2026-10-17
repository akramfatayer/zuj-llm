# Mini-assignment 1: Tokenizer Audit

**Course:** Large Language Models and Query Engineering · **Week 2** · Supports CLO1
**Weight:** 3% of the course grade · **Individual work** · **Due:** start of the week 3 lab session, on the LMS

## The question

You are advising a team that will build an Arabic question-answering assistant. Before they pick a model, they want to know: **which tokenizer handles Arabic best, and what does a poor one cost them?** Answer with measurements, not opinions.

## What to do

Start from your copy of the Lab 02 notebook. Lab work was done in pairs; this assignment is your own.

1. **Measure more tokenizers.** Add at least one tokenizer that we did not use in the lab, for example `google/mt5-small`, `facebook/nllb-200-distilled-600M` or `CAMeL-Lab/bert-base-arabic-camelbert-mix`. Report fertility (English, MSA, dialect) and the Arabic ÷ English token ratio for all six or more tokenizers, in one table and one chart.
2. **Test dialect properly.** Write 10 sentences of your own in your Arabic dialect, each with an MSA version and an English translation (30 sentences in total). Add them to the measurements. Does the dialect gap you saw in the lab hold up with more data?
3. **Test cross-lingual matching.** Using the lab's embedding model, match each Arabic sentence to its English translation and report top-1 accuracy separately for MSA (the lab's 20 pairs plus your 10: 30 pairs) and for dialect (the lab's 5 plus your 10: 15 sentences). Show two misses, if there are any, and explain each.
4. **Write the recommendation.** In 300–400 words: which tokenizer would you recommend for the team, and why? Explain your results with how tokenizers are trained (where the vocabulary comes from), and state the cost in concrete terms: tokens, GPU time, and how much Arabic text fits in a 4,096-token context window.

## What to submit

- Your notebook (`.ipynb`), run from top to bottom so that every output is visible.
- Your recommendation as a PDF (or as a markdown cell at the end of the notebook).
- A one-line AI-use disclosure: which tool you used, if any, and for what. You may be asked to explain any part of your work orally.

## How it is graded

Each criterion is scored 0, 1 or 2. The total (out of 8) is scaled to 3%.

| Criterion | 2 — complete | 1 — partial | 0 — missing |
|---|---|---|---|
| **Measurement** | Six or more tokenizers, correct fertility and ratio, clear table and chart | Fewer tokenizers, or errors in counting (e.g. special tokens included) | No new measurements |
| **Dialect data** | 30 own sentences, MSA and dialect compared with the lab's results | Some sentences, or no comparison | No own data |
| **Cross-lingual matching** | Accuracy for MSA and dialect separately, misses explained | Accuracy without explanation | Not done |
| **Recommendation** | Clear choice, explained with how tokenizers are trained, cost stated in tokens and context length | Choice given, but explanation or cost vague | Missing, or not based on the measurements |

**Late work:** 10% deduction per day, for up to three days (course policy).
