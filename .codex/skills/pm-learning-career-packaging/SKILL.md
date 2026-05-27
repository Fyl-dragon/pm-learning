---
name: pm-learning-career-packaging
description: Project-local skill for AI product manager career planning, resume packaging, portfolio storytelling, interview project preparation, and career asset conversion in the pm-learning repository. Use when Codex needs to turn learning outputs such as LLM Gateway, Eval Harness, RAG Evaluation Harness, Agent Harness, Harness productization, LLMOps quality governance, or industry AI scenarios into resume bullets, case studies, self-introductions, interview scripts, mock questions, or job-search positioning.
---

# PM Learning Career Packaging

Use this skill to convert project learning into career-facing evidence: resume bullets, interview stories, portfolio case studies, and role positioning.

Default language is Chinese.

## Context First

Before packaging, inspect:

- `.planning/PROJECT.md`
- `ai-fde-portfolio/career/resume-v1.md`
- `ai-fde-portfolio/career/interview-scripts.md`
- `ai-fde-portfolio/career/jd-analysis.md`
- Relevant project docs under `ai-fde-portfolio/docs/projects/`
- Relevant project implementation under `ai-fde-portfolio/projects/`

## Packaging Workflow

1. Identify the target role and interview audience.
2. Extract real project evidence from files; do not invent accomplishments.
3. Convert technical work into product value: user, problem, decision, metric, tradeoff, risk, outcome.
4. Produce the requested artifact: resume bullets, project case study, self-introduction, interview script, or Q&A.
5. Mark weak or missing evidence as `需要补证据`, not as finished experience.

## Default Positioning

Prioritize these directions unless the user says otherwise:

- AI platform PM / AI Evals & Harness product direction.
- LLMOps quality governance product manager.
- LLM platform product manager.
- RAG/Agent platform product manager.
- AI application product manager as secondary path.

## Artifact Rules

Use `references/packaging-rubric.md` before rewriting career material.

Resume bullets must:

- Start with a concrete action.
- Mention product/business/platform value.
- Include scope, metric, or observable output when available.
- Avoid exaggerated ownership or unverifiable numbers.
- Fit the target role's language.

Interview scripts must have 2/5/8/15-minute variants when requested and should cover:

- Background.
- Problem.
- Product design.
- Technical/AI quality choices.
- Tradeoffs and metrics.
- What the user personally contributed.
- What would be improved next.

## Quality Bar

- Do not create fake company experience or fake impact numbers.
- Do not write generic "负责需求分析" bullets.
- Tie each package to evidence in project files or mark evidence gaps.
- Make the user sound like a technical AI PM who understands platform governance and delivery reality.

## Resources

- `references/packaging-rubric.md`: resume and interview quality criteria.
- `assets/templates/interview-project-pack.md`: project interview package template.
- `assets/templates/resume-bullet-bank.md`: resume bullet template.
