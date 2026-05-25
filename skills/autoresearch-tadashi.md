# AutoResearchClaw Skill — Tadashi Version

## Purpose
Generate research-grade wiki content automatically using PRISMA-adapted methodology, web search, and structured analysis. Produces articles with zero AI-SLOP: no generic lists, no vague openings, no unsubstantiated claims.

## Quality Standards
- Minimum 4500 words per article
- Minimum 15 references with DOIs/clickable URLs
- 70% primary sources (peer-reviewed, institutional)
- Clear argumentative thesis, not descriptive summaries
- Quantitative data with specific numbers, not hand-waving
- Critical analysis: identify gaps, limitations, contradictions
- No phrases like: "In today's world", "It is important to note", "As we know"

## Methodology

### Phase 1: Discovery (30 min)
1. Search 3 angles on topic using web search
2. Extract 5-10 key sources (prioritize .edu, .gov, DOI links)
3. Identify: thesis, counter-thesis, data gaps, recent breakthroughs

### Phase 2: Outline (20 min)
1. Hypothesis-driven structure (not topic-driven)
2. Each section must advance the argument
3. Placeholder for: data tables, case studies, limitations

### Phase 3: Draft (90 min)
1. Write with source open side-by-side
2. Every claim needs [Author, Year, Source] inline
3. Include: comparison tables, quantitative metrics, edge cases
4. Flag uncertain claims with [VERIFY NEEDED]

### Phase 4: Review (20 min)
1. Check: word count, reference count, source quality
2. Remove all AI-SLOP phrases
3. Add explicit "Limitations" and "Future Research" sections

## Output Format
```markdown
---
slug: auto-{topic}-{date}
title: '{Thesis-driven title}'
authors: [eliza]
tags: [tag1, tag2, tag3]
---

# {Title}

**Abstract** (250 words max, structured: Context/Method/Result/Conclusion)

## 1. {Section advancing thesis}
...

## N. Conclusion

## Referências
- Author. (Year). Title. *Journal*, Vol(Issue), Pages. [DOI](url)

**Metodologia:** AutoResearchClaw v2.0
**Data:** YYYY-MM-DD
**Fontes primárias:** N/M total
**Licença:** CC BY-SA 4.0
```

## Topic Rotation (Weekly Cycle)
| Week | Theme | Audience |
|------|-------|----------|
| 1 | Market Analysis | Investors |
| 2 | Technical Deep-Dive | Engineers |
| 3 | Ethics/Policy | Academics |
| 4 | Case Study | General |

## Search Queries (Templates)
- Market: `"{topic}" market size CAGR 2024 2025 2030 billion`
- Tech: `"{topic}" architecture performance benchmark latency`
- Ethics: `"{topic}" regulation policy framework consent`
- Case: `"{topic}" implementation results ROI case study`

## Execution
Use web search for data, write to `/root/.openclaw/workspace/research-wiki/blog/`, commit to git, deploy via `npm run deploy`.
