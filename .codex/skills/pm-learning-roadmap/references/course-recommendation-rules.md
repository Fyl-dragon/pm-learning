# Course Recommendation Rules

Use these rules whenever recommending courses, books, videos, newsletters, repos, documents, or practice materials.

## Required Fields

Each recommendation must include:

- Priority: P0, P1, P2, P3, or P4
- Category: product mainline, AI Builder technical reinforcement, market/career, reference library, or excluded
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
- AI Builder technical resources must create runnable/interactable artifacts, tests/evals, and career-facing explanations.

## Project Priority Defaults

- P0: Must-study Chinese or Chinese-first resources that fill immediate foundations and map to a current artifact.
- P1: Mainline resources that directly produce Eval Harness, RAG Evaluation Harness, Agent Harness, LLMOps product artifacts, or selected AI Builder practice tied to those artifacts.
- P2: Selective official or high-quality English resources; use only with a clear chapter/scope and output.
- P3: Reference libraries and tool comparison targets; do not schedule continuous study.
- P4: Excluded or deprioritized resources, including broad course-platform catalogs and vague product homepages.

## AI Builder Boundaries

- Include: Python/FastAPI basics, simple frontend/prototype work, LLM API engineering, RAG engineering, Agent engineering, Evals/Harness, and AI-assisted development workflow.
- Exclude or downgrade: deep learning training, PyTorch model training, distributed training, CUDA, model fine-tuning engineering, complex frontend framework deep dives, algorithm drills, and cloud-native platform sprawl.
- Every AI Builder recommendation must answer: what runnable artifact, what test/eval/trace proof, and what interview expression it produces.

## Current Resource Baseline

- P0: Datawhale LLM Cookbook; Happy-LLM 第 7 章大模型应用部分; Datawhale LLM Universe.
- P1: FastAPI 中文文档; Hugging Face Agents Course 中文版; promptfoo Eval Guides; Langfuse docs/GitHub for product teardown; this project's LLM Gateway codebase; rohitg00/ai-engineering-from-scratch selected Phase 11/13/14/17 lessons.
- P2: OpenAI Evals; DeepLearning.AI Evaluating AI Agents.
- P3: Phoenix / DeepEval / RAGAS for tool comparison.
- P4: DeepLearning.AI full course catalog or any broad course/product portal without a concrete learning scope.

## rohitg00/ai-engineering-from-scratch Rules

- Recommend only selected lessons from Phase 11, 13, 14, and 17 that directly map to LLM Gateway, Eval Harness, RAG Evaluation Harness, Agent Harness, LLMOps, or AI Builder evidence.
- Never recommend full-curriculum study.
- Require the 5-step loop: read objective, run code, read key structure, modify one thing, migrate the insight into the pm-learning project.
- Mark math, model training, vision, audio, RL, distributed inference, GPU/CUDA, and low-level serving internals as P4 unless the user explicitly asks for that engineering path.
