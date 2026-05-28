---
name: pm-learning-roadmap
description: Project-local skill for AI product manager learning roadmap and course/resource recommendations in the pm-learning repository. Use when Codex needs to create or adjust monthly/weekly AI PM study plans, recommend courses or learning materials, map skill gaps to outputs, design study tasks for LLM platforms, AI Evals, Eval Harness, RAG evaluation, Agent Harness, LLMOps quality governance, AI Builder / AI-assisted development, or improve learning route quality with evidence constraints.
---

# PM Learning Roadmap

Use this skill to turn AI product manager growth goals into executable learning routes, course/resource recommendations, and weekly tasks that produce portfolio, resume, or interview assets.

Default language is Chinese.

## Context First

Before planning, read the relevant project files:

- `.planning/PROJECT.md`
- `README.md`
- `ai-fde-portfolio/plan/6-month-roadmap.md`
- `ai-fde-portfolio/plan/learning-resources-priority.md`
- `ai-fde-portfolio/plan/ai-builder-technical-track.md`
- `ai-fde-portfolio/plan/ai-engineering-from-scratch-study-plan.md`
- `ai-fde-portfolio/plan/month-01.md`
- `ai-fde-portfolio/plan/week-01.md`
- `ai-fde-portfolio/career/jd-analysis.md`
- `ai-fde-portfolio/career/resume-v1.md`

For project-specific technical learning, also inspect `ai-fde-portfolio/projects/` and `ai-fde-portfolio/docs/projects/`.

## Planning Workflow

1. Identify the target role direction: AI Evals / Harness, LLMOps, LLM platform PM, RAG/Agent platform PM, AI Builder-type PM, or industry AI PM.
2. Extract current route, current week, completed outputs, and gaps from project files.
3. Convert gaps into tasks with ability target, concrete output, time box, and acceptance check.
4. Recommend resources only when they directly support the next output.
5. For current courses/resources, browse or cite current sources and include snapshot dates.

## Course Recommendation Rules

Use `references/course-recommendation-rules.md` before recommending courses or resources.

Default strategy:

- Prefer Chinese, executable, low-cost resources first.
- Respect the P0/P1/P2/P3/P4 priority list in `ai-fde-portfolio/plan/learning-resources-priority.md`.
- For AI development topics, separate product-mainline resources from AI Builder technical reinforcement resources.
- Treat `rohitg00/ai-engineering-from-scratch` as a selected P1/P2 AI Builder practice library only for Phase 11/13/14/17 lessons that map to LLM Gateway, Eval Harness, RAG Evaluation Harness, Agent Harness, or LLMOps. Do not recommend full-curriculum study.
- Add English official/high-quality resources when Chinese options are weak or outdated.
- Recommend fewer resources with a clear use case; do not produce generic course dumps.
- Every resource must include name, link, source date, cost/time estimate, language barrier, concrete chapter/scope, why it fits, expected output, and an alternative.

## Output Requirements

Plans must include:

- Ability target.
- Learning task.
- Output artifact.
- Acceptance criteria.
- Review method.
- Relationship to resume, portfolio, or interview expression.

Use `assets/templates/learning-plan.md` for monthly or weekly plans.

## Quality Bar

- Do not replace the existing 6-month route unless the user asks for a redesign.
- Do not optimize for "learning more"; optimize for provable AI PM competitiveness.
- Do not recommend a course unless it maps to a near-term output.
- Do not recommend platform/product homepages as learning materials unless you also name the exact course, chapter, guide, docs page, or repository section to study.
- Do not turn AI Builder learning into a pure full-stack, algorithm, model-training, or cloud-native engineering route.
- Keep workload realistic for weekday morning/evening and weekend study rhythm.

## Resources

- `references/course-recommendation-rules.md`: evidence and formatting rules for resource recommendations.
- `references/learning-route-map.md`: preferred AI PM capability map for this project.
- `assets/templates/learning-plan.md`: plan template.
