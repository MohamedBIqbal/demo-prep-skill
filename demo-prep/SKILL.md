---
name: preparing-demos
description: Prepares product demos from technical walkthroughs to C-suite presentations — 5-minute format, pyramid structure, presenter scripts, checklists, Q&A frameworks, follow-up templates. Use when preparing a demo, creating presentation slides, writing a presenter script, or presenting to executives or investors.
user-invocable: false
---

# Demo Prep Skill

Prepares product demos — from technical walkthroughs to C-suite presentations.

## Quick Start

| Audience | Use This |
|----------|----------|
| Technical peers | [Technical Demo Format](#technical-demo-format) |
| Executives / Investors | [C-Suite Format](#c-suite-format) |
| Need PPTX slides | See [references/powerpoint-generation.md](references/powerpoint-generation.md) |
| Apple-style UI | See [references/apple-style-ui.md](references/apple-style-ui.md) |
| Glassmorphism slides | See [references/glassmorphism.md](references/glassmorphism.md) |

## Technical Demo Format (5-Minute)

| Segment | Duration | Content |
|---------|----------|---------|
| 1. Hook + Problem | 1 min | Why this matters, the pain point |
| 2. Solution | 30 sec | Architecture, key components |
| 3. Live Demo | 2 min | Concrete example, show it working |
| 4. Results | 30 sec | Metrics, test coverage, proof |
| 5. Challenges + Next | 30 sec | Honest roadmap |
| 6. The Ask | 30 sec | What you need from the audience |

**Deliverables:** Interactive HTML, presenter script with timing, terminal demo script.

**Tips:** Start with WHY. Show, don't tell. One thing per slide. Practice transitions. End with a clear ask.

## C-Suite Format

**Core principle:** Executives want to make decisions, not absorb information. Every element should answer: "What do you want me to do about this?"

**Pyramid Structure:** Recommendation → Key Points → Evidence (if asked). Never: Evidence → Analysis → Conclusion.

**Opening template:**
> "[Product] solves [specific problem] for [audience]. I need [your ask]. Here's proof."

**The 30/70 Rule:** 30% presenting, 40% demonstrating, 30% discussion/Q&A.

**The "So What?" Test:**

| Technical | Executive Translation |
|-----------|----------------------|
| Hallucination detection | Prevents AI from making things up |
| RBAC enforcement | Only authorized users see their data |
| Audit trail | Complete paper trail for regulators |

## Pre-Demo Checklist

### Content
- [ ] Can you state your ask in ONE sentence?
- [ ] Does slide 1 contain your recommendation?
- [ ] Have you removed all jargon?
- [ ] Is every number tied to business impact?

### Delivery
- [ ] Practiced with timer?
- [ ] Backup plan if live demo fails?
- [ ] Prepared for top 3 objections?

### Technical
- [ ] Demo works offline/with backup?
- [ ] Font size readable from back of room?

## Handling Q&A: P.R.E.P. Framework

| Step | Action | Example |
|------|--------|---------|
| **P**oint | State your answer | "Yes, this is production-ready." |
| **R**eason | One supporting reason | "We've validated with 33 automated tests." |
| **E**xample | Concrete proof | "Hallucination detection catches 100%." |
| **P**oint | Restate conclusion | "So yes, ready for pilot deployment." |

## Red Flags to Avoid

| Don't | Do Instead |
|-------|------------|
| "Let me explain how this works..." | "Watch what happens when..." |
| Starting with company history | Start with their problem |
| Reading slides aloud | Use slides as visual anchors |
| Ending with "Any questions?" | End with your ask, then invite questions |

## Script Templates

**C-Suite Opening (30 sec):**
"[Name], thank you for your time. Today I'll show you [Product] — [one-sentence value prop]. I have one ask: [specific request]. Let me show you why."

**Technical Opening (30 sec):**
"[Problem context in one sentence]. I built [Product] to solve this. Let me show you how it works."

## Post-Demo Follow-up

```
Subject: [Product] Demo Follow-up — [Specific Ask]

[Name], Thank you for your time today. As discussed:
The Problem: [One sentence]
Our Solution: [One sentence]
The Proof: [Key metric]

Next Steps:
1. [Action] — [Owner] — [Date]

My Ask: [Restate clearly]
```

## Reference Files

- **[PowerPoint Generation](references/powerpoint-generation.md)**: PPTX structure, python-pptx API, slide design guidelines
- **[Apple Style UI](references/apple-style-ui.md)**: Typography, color palette, spacing, components, motion, layout patterns
- **[Glassmorphism](references/glassmorphism.md)**: Glass effects, animated backgrounds, layered compliance slides, CSS templates
