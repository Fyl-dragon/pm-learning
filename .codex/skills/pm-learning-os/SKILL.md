---
name: pm-learning-os
description: Project-local operating-system skill for the pm-learning repository. Use when Codex needs to plan or coordinate AI product manager learning, choose the right project skill, improve learning roadmap quality, prevent unsupported recommendations, route requests about courses, weekly evaluation, supervision, job-market research, career planning, interview project preparation, resume packaging, or any cross-cutting AI PM career-growth task inside this project.
---

# PM Learning OS

Use this skill as the control layer for the `pm-learning` project. It keeps AI-generated advice grounded in the user's actual goal: turning product learning into provable AI product manager career competitiveness.

Default language is Chinese.

## Required Context

Before giving advice, read the relevant project files. Start with:

- `/Users/fengyonglong/workspace/code/pm-learning/.planning/PROJECT.md`
- `/Users/fengyonglong/workspace/code/pm-learning/README.md`
- `/Users/fengyonglong/workspace/code/pm-learning/ai-fde-portfolio/plan/6-month-roadmap.md`
- `/Users/fengyonglong/workspace/code/pm-learning/ai-fde-portfolio/plan/learning-resources-priority.md`
- `/Users/fengyonglong/workspace/code/pm-learning/ai-fde-portfolio/plan/ai-builder-technical-track.md`
- `/Users/fengyonglong/workspace/code/pm-learning/ai-fde-portfolio/plan/ai-engineering-from-scratch-study-plan.md`
- `/Users/fengyonglong/workspace/code/pm-learning/ai-fde-portfolio/plan/month-01.md`
- `/Users/fengyonglong/workspace/code/pm-learning/ai-fde-portfolio/plan/week-01.md`
- `/Users/fengyonglong/workspace/code/pm-learning/ai-fde-portfolio/career/jd-analysis.md`
- `/Users/fengyonglong/workspace/code/pm-learning/ai-fde-portfolio/career/resume-v1.md`
- `/Users/fengyonglong/workspace/code/pm-learning/ai-fde-portfolio/career/interview-scripts.md`

If a file is missing, continue from available context and list the missing file under `待确认问题`.

## Routing

Route work to the most specific project skill:

- Use `$pm-learning-roadmap` for learning routes, weekly/monthly plans, course recommendations, and study resource selection.
- Use `$pm-learning-evaluator` for weekly review, learning-effect scoring, supervision, accountability, and reminder setup.
- Use `$pm-learning-market-research` for current job-market, interview requirements, salary, company, and opportunity research.
- Use `$pm-learning-career-packaging` for career positioning, resume bullets, project packaging, interview scripts, and mock interview prep.
- Stay in `$pm-learning-os` when the request spans multiple domains or requires deciding the next best action.

## Evidence Contract

Never present current external information from memory. For courses, job postings, salary, company hiring signals, interview requirements, model/product-market trends, or policy changes:

- Browse or use current sources when available.
- Include source links and absolute snapshot dates.
- Mark unverified content as `推断假设` or `待验证`.
- If browsing is unavailable or the user asks for offline work, explicitly say the output is based only on project context and may need later verification.

Use the output labels in `references/output-contract.md` for substantial answers.

## Operating Workflow

1. Read project context first.
2. Classify the request and route to a specialist skill when useful.
3. State what is confirmed from project files.
4. Verify external/current facts before recommending.
5. Produce an artifact, not only advice: plan, rubric, research snapshot, resume bullets, interview script, or next-week action list.
6. End with 1-3 concrete next actions tied to the user's AI PM competitiveness.

## Quality Bar

- Advice must connect to AI Evals / Harness / LLMOps, AI platform product, RAG/Agent platform, LLM platform competitiveness, or AI Builder capability.
- Learning plans must include ability target, output artifact, acceptance check, and review method.
- AI development advice must keep the user positioned as an AI Builder-type product manager, not a pure full-stack engineer.
- Course/resource recommendations must follow the project's priority rules: Chinese first, short path first, portfolio output first, with concrete chapter/scope and language barrier.
- Market/career guidance must distinguish facts, assumptions, and recommendations.
- Do not generate generic self-improvement plans that ignore the repository's existing roadmap and portfolio.

## Resources

- `references/output-contract.md`: standard labels for facts, assumptions, sources, and next actions.
- `references/skill-routing.md`: routing rules and example requests.
- `assets/templates/weekly-ai-pm-operating-review.md`: compact weekly operating review template.
