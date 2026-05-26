---
name: pm-learning-roadmap
description: Project-local skill for AI product manager learning roadmap and course/resource recommendations in the pm-learning repository. Use when Codex needs to create or adjust monthly/weekly AI PM study plans, recommend courses or learning materials, map skill gaps to outputs, design study tasks for LLM platforms, RAG evaluation, Agent Harness, AI solution/FDE work, or improve learning route quality with evidence constraints.
---

# PM Learning Roadmap

Use this skill to turn AI product manager growth goals into executable learning routes, course/resource recommendations, and weekly tasks that produce portfolio, resume, or interview assets.

Default language is Chinese.

## Context First

Before planning, read the relevant project files:

- `.planning/PROJECT.md`
- `README.md`
- `ai-fde-portfolio/plan/6-month-roadmap.md`
- `ai-fde-portfolio/plan/month-01.md`
- `ai-fde-portfolio/plan/week-01.md`
- `ai-fde-portfolio/career/jd-analysis.md`
- `ai-fde-portfolio/career/resume-v1.md`

For project-specific technical learning, also inspect `ai-fde-portfolio/projects/` and `ai-fde-portfolio/docs/projects/`.

## Planning Workflow

1. Identify the target role direction: AI PM, AI solution, FDE, LLM platform PM, or industry AI PM.
2. Extract current route, current week, completed outputs, and gaps from project files.
3. Convert gaps into tasks with ability target, concrete output, time box, and acceptance check.
4. Recommend resources only when they directly support the next output.
5. For current courses/resources, browse or cite current sources and include snapshot dates.

## Course Recommendation Rules

Use `references/course-recommendation-rules.md` before recommending courses or resources.

Default strategy:

- Prefer Chinese, executable, low-cost resources first.
- Add English official/high-quality resources when Chinese options are weak or outdated.
- Recommend fewer resources with a clear use case; do not produce generic course dumps.
- Every resource must include name, link, source date, cost/time estimate, why it fits, and an alternative.

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
- Keep workload realistic for weekday morning/evening and weekend study rhythm.

## Resources

- `references/course-recommendation-rules.md`: evidence and formatting rules for resource recommendations.
- `references/learning-route-map.md`: preferred AI PM capability map for this project.
- `assets/templates/learning-plan.md`: plan template.
