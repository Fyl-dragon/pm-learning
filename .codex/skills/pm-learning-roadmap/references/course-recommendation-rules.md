# Course Recommendation Rules

Use these rules whenever recommending courses, books, videos, newsletters, repos, documents, or practice materials.

## Required Fields

Each recommendation must include:

- Priority: P0, P1, P2, P3, or P4
- Name
- Link
- Source or publisher
- Snapshot date
- Cost level: free, low-cost, paid, unknown
- Time investment
- Language barrier: Chinese, Chinese translation, English short docs, English video, subtitles unknown, or unknown
- Concrete scope: course, chapter, unit, docs page, guide, or repo section
- Why it fits the user's current route
- What output it should produce
- Alternative option

## Evidence Rules

- Current course availability, pricing, syllabus, and enrollment details must be verified from current sources.
- Prefer official course pages, university/vendor docs, reputable platform pages, or source repositories.
- If only memory/project context is used, label recommendations as offline hypotheses.
- Do not invent course names, instructors, prices, URLs, or certificates.
- If subtitle/transcript availability is not verified, mark it as "字幕未确认" and lower the priority for English video resources.

## Selection Defaults

- Chinese executable resources first.
- Short, concrete learning paths before broad platforms or full course catalogs.
- English official docs or high-quality references when they are more accurate or necessary.
- Low-cost or free first, unless paid material clearly saves time and maps to a deliverable.
- Prefer resources that help create project artifacts: PRD, eval harness, case study, prototype, interview script, or resume bullet.

## Project Priority Defaults

- P0: Must-study Chinese or Chinese-first resources that fill immediate foundations and map to a current artifact.
- P1: Mainline resources that directly produce Eval Harness, RAG Evaluation Harness, Agent Harness, or LLMOps product artifacts.
- P2: Selective official or high-quality English resources; use only with a clear chapter/scope and output.
- P3: Reference libraries, engineering-heavy repositories, and tool comparison targets; do not schedule continuous study.
- P4: Excluded or deprioritized resources, including broad course-platform catalogs and vague product homepages.

## Current Resource Baseline

- P0: Datawhale LLM Cookbook; Happy-LLM 第 7 章大模型应用部分.
- P1: Hugging Face Agents Course 中文版; promptfoo Eval Guides; Langfuse docs/GitHub for product teardown.
- P2: OpenAI Evals; DeepLearning.AI Evaluating AI Agents.
- P3: rohitg00/ai-engineering-from-scratch; Phoenix / DeepEval / RAGAS for tool comparison.
- P4: DeepLearning.AI full course catalog or any broad course/product portal without a concrete learning scope.
