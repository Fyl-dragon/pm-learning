---
name: pm-learning-market-research
description: Project-local skill for current AI product manager job-market, interview, salary, company, and opportunity research for the pm-learning repository. Use when Codex needs to investigate AI Evals, Eval Harness, LLMOps, AI observability, AI Builder-type PM, LLM platform PM, RAG/Agent product, AI solution, FDE risk, or local Chongqing job requirements, identify market skill gaps, analyze JDs, compare role expectations, or source evidence for learning and career decisions.
---

# PM Learning Market Research

Use this skill to turn current market evidence into learning priorities, portfolio decisions, and interview-preparation targets.

Default language is Chinese.

## Evidence Is Mandatory

For market, role, salary, company, interview, and course-demand claims:

- Browse or use current sources unless the user explicitly asks for offline work.
- Include source links and absolute snapshot dates.
- Prefer official/company career pages, job boards, reputable reports, and actual JD text.
- Do not invent companies, openings, salary bands, hiring trends, or interview questions.
- Mark low-confidence findings as `样本有限` or `待验证`.

Use `references/research-protocol.md` before producing a market snapshot.

## Research Workflow

1. Read project goals and current resume/JD analysis.
2. Define role scope: AI Evals / Harness, LLMOps, AI observability, AI Builder-type PM, LLM platform PM, RAG/Agent platform PM, AI solution, FDE risk, or local industry AI role.
3. Gather current sources and record snapshot date.
4. Extract repeated requirements: domain, AI systems, product methods, delivery, tools, language, salary, location.
5. Compare requirements against the user's current assets.
6. Output learning priorities and career-packaging implications.

## Default Research Targets

- Chongqing and nearby opportunities when location matters.
- Remote or national roles only when they clarify skill requirements or offer realistic alternatives.
- AI Evals / Harness, LLMOps, AI observability, LLM platform PM, RAG/Agent product roles.
- AI Builder-type PM roles that require hands-on prototyping, coding tools, API understanding, tests, evals, or technical fluency.
- AI solution and FDE only as filtered backup roles; exclude pure onsite implementation, customer success, delivery rescue, and presales support.

## Output Requirements

Use `assets/templates/market-research-snapshot.md` for structured research.

Always include:

- Sample size and source list.
- Snapshot date.
- High-frequency requirements.
- User already has / needs to build / should package better.
- Implications for next learning plan and interview prep.

## Quality Bar

- Prefer exact JD language over paraphrased market stereotypes.
- Keep conclusions proportional to evidence.
- Do not recommend changing career direction from a small sample.
- Convert market findings into actionable learning and packaging changes.

## Resources

- `references/research-protocol.md`: market research rules and source hierarchy.
- `assets/templates/market-research-snapshot.md`: output template.
