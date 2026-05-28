---
name: pm-learning-evaluator
description: Project-local skill for evaluating and supervising AI product manager learning progress in the pm-learning repository. Use when Codex needs to review weekly learning results, score AI PM skill growth, compare planned versus actual outputs, create improvement actions, supervise study cadence, define acceptance criteria, or set up reminders/follow-ups for learning review.
---

# PM Learning Evaluator

Use this skill to judge whether learning has become provable AI PM competitiveness: portfolio output, product reasoning, interview expression, and target-role fit.

Default language is Chinese.

## Context First

Read the current plan and evidence before scoring:

- `.planning/PROJECT.md`
- `ai-fde-portfolio/plan/6-month-roadmap.md`
- `ai-fde-portfolio/plan/month-01.md`
- `ai-fde-portfolio/plan/week-01.md`
- `ai-fde-portfolio/career/resume-v1.md`
- `ai-fde-portfolio/career/interview-scripts.md`
- `ai-fde-portfolio/evaluations/`
- Relevant project and docs folders for the artifact being evaluated.

## Evaluation Workflow

1. Extract planned goals and expected outputs.
2. Inspect actual outputs and learning evidence.
3. Score with `references/evaluation-rubric.md`.
4. Identify the smallest next correction that improves career competitiveness.
5. Produce a review artifact using `assets/templates/weekly-review.md` for weekly reviews.

## Scoring Defaults

Use a 0-5 score for each dimension:

- Plan completion.
- Artifact quality.
- AI PM reasoning depth.
- Interview/resume transferability.
- Market-role fit.
- Next-step clarity.

Do not inflate scores. A high score requires visible artifacts, not good intentions.

## Supervision And Reminders

When the user asks for reminders, supervision, recurring check-ins, or follow-ups:

- Use the available Codex automation/reminder tool.
- Default cadence: every Sunday morning in the user's locale for weekly learning review.
- Prompt should ask the future agent to read the project plan, inspect the week's outputs, score progress, and propose next week's top 3 actions.
- Do not create reminders unless the user explicitly asks for them.

## Quality Bar

- Treat missing artifacts as a finding, not as proof of failure.
- Link each criticism to a concrete improvement action.
- Prefer one high-leverage adjustment over a long list of vague suggestions.
- Always connect review output to AI PM competitiveness.
- Save substantial weekly or midweek reviews under `ai-fde-portfolio/evaluations/` when the user asks to persist project learning evidence or when continuing the project goal.

## Resources

- `references/evaluation-rubric.md`: scoring dimensions and interpretation.
- `assets/templates/weekly-review.md`: weekly review template.
