# Team Project: An LLM Application with Retrieval and Tools

**Course:** Large Language Models and Query Engineering · **Released:** week 3 · Supports CLO3–CLO7
**Weight:** 30% of the course grade, in five phases · **Teams of 3–4** · **Final demos:** week 15

## The task

Choose a real problem, ideally one that involves Arabic text, and build an application that:

1. **answers from documents it retrieves**: a collection your team assembles, with the answer citing the passages it used;
2. **calls at least one tool**: for example a SQL database, a calculator or a public web API, chosen by the model when a question needs it;
3. **runs on open-weight models only**, in the department's GPU lab or on Google Colab, with no paid API;
4. **is measured**: on a test set your team writes, for answer quality, faithfulness to the sources, tool-call success, cost and safety.

You will learn the pieces as the course goes: prompting in weeks 6–8, retrieval in weeks 9–10, tools and agents in week 11, evaluation in week 12 and red-teaming in week 13. What you need now is a team, a problem and a source of documents.

## Phases and deadlines

| When | Phase | What you hand in | Weight |
|---|---|---|---|
| Week 4 lab | — | Team of 3–4 registered on Moodle, with a working title | — |
| Week 7 | **1 · Proposal and data plan** | A 2-page proposal (template below) | 3% |
| Week 10 | **2 · Dataset and test set** | The document collection, the test set and a one-page datasheet | 3% |
| Week 12 | **3 · Working prototype** | A live demo in the lab and a repository that runs from its README | 4% |
| Week 14 | **4 · Evaluation and red-team report** | Results on the test set and a red-team log, 3–4 pages | 4% |
| Week 15 | **5 · Final demo, report and code** | A 10-minute demo, a report of at most 8 pages, the final code | 16% |

Phases 1–4 are due at the start of that week's lab session. Late work loses 10% per day, up to three days, and is not accepted afterwards without a documented excuse.

## Example projects

These show the expected size. You may take one, adapt one or propose your own.

| Project | Documents | Tool |
|---|---|---|
| **ZUJ study assistant** (Arabic): answers students' questions about regulations and study plans | The university's public regulations and study-plan pages | SQL over a course table: prerequisites, credit hours, which semester a course is offered |
| **Jordan visitor guide** (Arabic and English) | Public tourism pages about Petra, Wadi Rum, Jerash and the Dead Sea | A weather API that needs no key (e.g. Open-Meteo) or a travel-distance calculator |
| **Labour-law helper** (Arabic) | The public text of the Jordanian Labour Law and official guidance | A calculator for leave days or end-of-service pay. The app must say that it is not legal advice. |
| **Course tutor** for one of your own courses | Lecture slides and notes you are allowed to use | A question bank in SQLite: the app quizzes the student and checks answers |
| **Water and climate facts** (Arabic and English) | Public reports from Jordanian and international agencies | SQL over an open dataset, e.g. rainfall or water use by governorate |
| **Recipe and nutrition helper** (Arabic) | Recipes you are allowed to use | A nutrition table: calories and macros for a recipe and a serving size |

## Rules

- **Models:** open-weight models only (for example Qwen2.5-1.5B, 3B or 7B Instruct, quantised if needed), and a multilingual embedding model. Respect each model's licence.
- **Data:** public or properly licensed documents only, with the source and licence recorded in your datasheet. No personal data about real people.
- **Compute:** everything must run in the GPU lab or on a free Colab T4. If your design needs more, simplify it.
- **AI assistants:** allowed for brainstorming, debugging and editing, with a short disclosure in each submission stating which tool you used and for what. Every member must be able to explain any part of the code or report; work no member can explain is graded as not the team's.
- **Contribution:** the final report ends with a contribution statement signed by every member. The instructors may adjust an individual's Phase 5 mark when the statements and the repository history show a clearly unequal share.

## Phase 1 · Proposal and data plan (week 7, 3%)

At most two pages:

1. **Problem and users:** who needs this, and what do they do today without it?
2. **Ten example questions** your users would ask, at least five in Arabic if your project is Arabic, including at least two that need the tool.
3. **Documents:** where they come from, how many you expect, their licence, and how you will collect and clean them.
4. **Tool:** what it does, what data it uses, and an example of a question that needs it.
5. **Risks:** what could go wrong (data access, wrong answers that could harm a user, prompt injection) and what you will do about it.
6. **Roles:** who leads data, retrieval, the tool and evaluation. Everyone writes code.

| Criterion | 2 — complete | 1 — partial | 0 — missing |
|---|---|---|---|
| **Problem** | Real users and a clear need | Vague users or need | Missing |
| **Questions** | Ten realistic questions, tool questions included | Fewer, or all of one kind | Missing |
| **Data plan** | Sources named, licence checked, size estimated | Sources named only | Missing |
| **Tool and risks** | Tool justified by example questions; risks with responses | One of the two thin | Missing |

## Phase 2 · Dataset and test set (week 10, 3%)

- **Document collection:** cleaned text, ready to split into chunks, with one record per document (title, source URL, licence, date, language). Aim for at least 50 documents or 100 pages.
- **Test set:** at least 40 questions with a reference answer and the document that supports it. Include at least 10 questions that need the tool, at least 5 that your documents **cannot** answer (the right response is "I don't know"), and, for an Arabic project, at least half in Arabic.
- **Datasheet (one page):** what the collection covers and what it leaves out, how it was collected, known gaps and biases.

| Criterion | 2 — complete | 1 — partial | 0 — missing |
|---|---|---|---|
| **Collection** | Clean, documented, large enough to need retrieval | Small, or poorly documented | Missing |
| **Test set** | 40+ questions with references, tool and unanswerable questions included | Fewer, or missing a category | Missing |
| **Datasheet** | Coverage, collection and gaps described honestly | Partial | Missing |

## Phase 3 · Working prototype (week 12, 4%)

Show it working end to end in the lab: a question goes in, passages are retrieved, the tool is called when needed, and the answer comes back with citations. Submit a repository whose README lets another team run it on Colab.

| Criterion | 2 — complete | 1 — partial | 0 — missing |
|---|---|---|---|
| **Retrieval** | Retrieves relevant passages and cites them in the answer | Retrieves, but citations missing or wrong | Missing |
| **Tool call** | The model calls the tool correctly when a question needs it | Tool works only when forced, or fails often | Missing |
| **Runs from the README** | Another team can run it | Runs with help | Does not run |

## Phase 4 · Evaluation and red-team report (week 14, 4%)

3–4 pages, using the methods of weeks 12 and 13:

- **Evaluation:** run the whole test set. Report answer correctness, faithfulness to the retrieved sources, citation accuracy, tool-call success, and how often the system says "I don't know" when it should. Add latency and token cost per question. If you use an LLM as a judge, check it against your own judgement on at least 20 answers.
- **Red-team log:** at least 10 attempts to break your system, including prompt injection hidden in a document and attempts to make it misuse the tool, in English and in Arabic. For each attempt: what you tried, what happened and what you changed.

| Criterion | 2 — complete | 1 — partial | 0 — missing |
|---|---|---|---|
| **Metrics** | All the measures above, on the full test set | Some measures, or part of the test set | Missing |
| **Judge check** | LLM judge compared with human judgement | Judge used without a check | No judge and no human scoring |
| **Red-team** | 10+ attempts in both languages, with fixes | Fewer, or no fixes | Missing |
| **Error analysis** | Failures grouped by cause, with examples | Failures listed only | Missing |

## Phase 5 · Final demo, report and code (week 15, 16%)

- **Demo:** 10 minutes plus 5 minutes of questions. Every member presents a part.
- **Report:** at most 8 pages: the problem, the design and why you chose it, the final evaluation (updated from Phase 4), what you would do with more time, the AI-use disclosure and the contribution statement.
- **Code:** the final repository, tagged, running from its README.

| Criterion | Weight | Excellent | Adequate | Weak |
|---|---|---|---|---|
| **Problem and design** | 20% | A real need; design choices justified with evidence (e.g. a chunk size or model chosen by measurement) | Reasonable design, little justification | Unclear problem or design |
| **Implementation** | 30% | Retrieval, tool use and generation work reliably; clean, documented code | Works with gaps or fragile parts | Partly working |
| **Evaluation** | 25% | Full test set, sound metrics, honest error analysis; Arabic evaluated in Arabic | Metrics present but thin or one-sided | Little or no evaluation |
| **Report** | 10% | Clear, complete, within length | Complete but unclear in places | Missing parts |
| **Presentation and contribution** | 15% | Clear live demo; every member answers questions on any part | Demo works; uneven answers | Demo fails or members cannot explain the work |

Projects that use Arabic-language data and evaluate in Arabic are preferred, and the rubric credits that work in problem and design and in evaluation.

## Getting started this week

1. Form a team of 3–4 and register it on Moodle before the week 4 lab.
2. Pick a problem and check, before anything else, that you can legally get the documents.
3. Write down ten questions a real user would ask. If you cannot, choose another problem.
