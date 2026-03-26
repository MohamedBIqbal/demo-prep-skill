# Demo Prep Skill

A comprehensive skill for preparing product demos — from technical walkthroughs to C-suite presentations.

## When to Use

Use this skill when you need to:
- Prepare a 5-minute product demo
- Create presentation slides (HTML or PowerPoint)
- Write a presenter script with timing
- Structure a demo for video recording
- Present to executives or investors

---

## Quick Start

| Audience | Use This |
|----------|----------|
| Technical peers | [Technical Demo Format](#technical-demo-format) |
| Executives / Investors | [C-Suite Format](#c-suite-format) |

---

# Technical Demo Format

## Demo Structure (5-Minute Format)

| Segment | Duration | Content |
|---------|----------|---------|
| 1. Hook + Problem | 1 min | Why this matters, the pain point |
| 2. Solution | 30 sec | Architecture, key components |
| 3. Live Demo | 2 min | Concrete example, show it working |
| 4. Results | 30 sec | Metrics, test coverage, proof |
| 5. Challenges + Next | 30 sec | Honest roadmap |
| 6. The Ask | 30 sec | What you need from the audience |

## Deliverables

1. **Interactive HTML** (`templates/interactive.html`) — Live presentation with timer and optional API calls
2. **Presenter Script** (`templates/script.md`) — What to say, timing markers
3. **C-Suite Script** (`templates/script-csuite.md`) — Executive-focused script with objection prep
4. **Terminal Demo** (`templates/demo.sh`) — Bash script for terminal-based demos with modular sections
5. **PowerPoint** (`demo.pptx`) — Generated from `scripts/generate_pptx.py` (10 slides, multiple palettes)

## Tips for Technical Demos

1. **Start with WHY** — Hook them in the first 10 seconds
2. **Show, don't tell** — Live demo > slides
3. **One thing per slide** — Don't overwhelm
4. **Practice the transitions** — Smooth flow matters
5. **End with a clear ask** — What do you want from them?

---

# C-Suite Format

## Core Principle: Decision-First

Executives don't want information — they want to make decisions. Every demo element should answer: **"What do you want me to do about this?"**

## Pyramid Structure (Lead with the Answer)

```
Traditional (WRONG for execs):
  Evidence → Analysis → Conclusion

Executive (RIGHT):
  Recommendation → Key Points → Evidence (if asked)
```

**Opening template:**
> "[Product] solves [specific problem] for [audience]. I need [your ask]. Here's proof."

## The 30/70 Rule

| Activity | Time Allocation |
|----------|-----------------|
| Presenting/talking | 30% |
| Showing/demonstrating | 40% |
| Discussion/Q&A hooks | 30% |

For a 5-minute demo:
- 90 seconds: Setup + ask
- 2 minutes: Live demo
- 90 seconds: Results + next steps + discussion opener

## Executive Attention Patterns

| Time | Attention Level | What to Show |
|------|-----------------|--------------|
| 0:00-0:30 | Peak | Your ONE key message + ask |
| 0:30-2:00 | High | Live demo / proof |
| 2:00-4:00 | Declining | Results + credibility |
| 4:00-5:00 | Second peak | Clear ask + next steps |

## The "So What?" Test

After every statement, ask: **"So what?"**

| Technical | Executive Translation |
|-----------|----------------------|
| Hybrid retrieval algorithm | Finds the right answer faster |
| 99.5% uptime SLA | Always available when you need it |
| End-to-end encryption | Your data stays private |
| 50ms response time | Instant results |
| Audit logging | Complete paper trail for regulators |

---

## Pre-Demo Checklist

### Content
- [ ] Can you state your ask in ONE sentence?
- [ ] Does slide 1 contain your recommendation?
- [ ] Have you removed all jargon?
- [ ] Is every number tied to business impact?
- [ ] Do you have a "leave-behind" summary?

### Delivery
- [ ] Practiced with timer?
- [ ] Backup plan if live demo fails?
- [ ] Prepared for top 3 objections?
- [ ] Know names/roles of attendees?

### Technical
- [ ] Demo works offline/with backup?
- [ ] Font size readable from back of room?
- [ ] No notifications/popups during demo?

---

## Handling Q&A: P.R.E.P. Framework

| Step | Action | Example |
|------|--------|---------|
| **P**oint | State your answer | "Yes, this is production-ready." |
| **R**eason | One supporting reason | "We've validated with automated tests." |
| **E**xample | Concrete proof | "Detection catches issues 100% of the time." |
| **P**oint | Restate conclusion | "So yes, it's ready for pilot deployment." |

---

## Common Executive Questions

1. **"What's this going to cost me?"** (TCO, resources, time)
2. **"What's the risk if we don't do this?"** (regulatory, competitive)
3. **"Who else is using this?"** (social proof, case studies)
4. **"What could go wrong?"** (honest risks + mitigations)
5. **"What do you need from me?"** (clear, specific ask)

---

## Demo Script Templates

### C-Suite Opening (30 sec)
```
"[Audience name], thank you for your time.

Today I'll show you [Product] — [one-sentence value prop].

I have one ask: [specific request].

Let me show you why."
```

### Technical Opening (30 sec)
```
"[Problem context in one sentence].

I built [Product] to solve this.

Let me show you how it works."
```

---

## Red Flags to Avoid

| Don't | Do Instead |
|-------|------------|
| "Let me explain how this works..." | "Watch what happens when..." |
| Starting with company history | Start with their problem |
| Reading slides aloud | Use slides as visual anchors |
| Apologizing for technical issues | Have backup ready, move on |
| Ending with "Any questions?" | End with your ask, then invite questions |
| Using acronyms without definition | Plain language first, term second |

---

## Post-Demo Follow-up Template

```markdown
Subject: [Product] Demo Follow-up — [Specific Ask]

[Name],

Thank you for your time today. As discussed:

**The Problem:** [One sentence]
**Our Solution:** [One sentence]
**The Proof:** [Key metric]

**Next Steps:**
1. [Action] — [Owner] — [Date]
2. [Action] — [Owner] — [Date]

**My Ask:** [Restate clearly]

I've attached [leave-behind document].

[Your name]
```

---

# HTML Presentation Features

## Built-in Timer

The interactive HTML template includes a presentation timer:

### Timer Presets
| Duration | Use Case |
|----------|----------|
| 3 min | Lightning talk, elevator pitch |
| 5 min | Standard demo (recommended) |
| 7 min | Extended demo with Q&A buffer |
| Custom | 1-30 minutes, set your own |

### Keyboard Shortcuts
| Key | Action |
|-----|--------|
| `T` | Open/close timer configuration |
| `S` | Start/stop timer |
| `←` `→` | Navigate slides |
| `N` | Toggle speaker notes |

### Visual Alerts
- **Normal:** White background
- **Warning (2 min):** Amber background
- **Danger (1 min):** Red background

### Auto-Start
Timer automatically starts when you advance from slide 1, so you can set up before the clock starts.

## Keyboard Navigation

| Key | Action |
|-----|--------|
| `→` or `Space` | Next slide |
| `←` | Previous slide |
| `N` | Toggle speaker notes |
| `T` | Timer configuration |
| `S` | Start/stop timer |
| `Escape` | Close modals |

---

# Slide Design Guidelines

## McKinsey Pyramid Principle

Each slide should follow:
1. **Action Title** — The takeaway (not a topic label)
2. **Visual Proof** — Charts, diagrams, screenshots
3. **Supporting Details** — Only if needed

## Typography

- **Title:** 28-36pt, bold
- **Subtitle:** 18-24pt
- **Body:** 14-18pt
- **Max 6 words per bullet**
- **Max 6 bullets per slide**

## Color Palettes (Story-Based Themes)

Choose a palette based on your storytelling approach:

### Default Palette — Corporate Professional

| Color | Hex | Use |
|-------|-----|-----|
| Primary Blue | #0066CC | Headers, emphasis |
| Dark Gray | #1E293B | Body text |
| Success Green | #10B981 | Positive metrics |
| Warning Amber | #D97706 | Caution, attention |
| Danger Red | #DC2626 | Risks, problems |
| Light Gray | #F8FAFC | Backgrounds |

**When to use:** Standard demos, technical audiences, corporate presentations.

### Iceberg Palette — Hidden Costs Storytelling

| Color | Hex | Use |
|-------|-----|-----|
| Sky | #E0F2FE | Above water (visible) |
| Sky Mid | #BAE6FD | Labels in sky zone |
| Ocean | #0284C7 | Water line transition |
| Ocean Deep | #0C4A6E | Below water (hidden) |
| Accent Orange | #F97316 | The visible cost number |
| Text Light | #FFFFFF | Text on dark ocean |

**When to use:** Demos that reveal hidden costs, compliance risks, or "tip of the iceberg" problems. The visual metaphor shows the audience what they see vs. what's lurking beneath.

**Example narrative:**
> "That $2.3M fine? That's just what you can see above the waterline. Below the surface: months of remediation, lost customer trust, and regulatory scrutiny."

### Using Palettes in PPTX

```bash
# Default corporate theme
python scripts/generate_pptx.py --output demo.pptx

# Iceberg storytelling theme (for hidden costs narrative)
python scripts/generate_pptx.py --output demo.pptx --palette iceberg
```

The iceberg palette automatically applies to slide 2 (The Problem) with sky/ocean visualization.

## Slide Templates

1. **Title Slide** — Product name, one-line value prop, your ask
2. **Problem Slide** — Pain point with visual contrast
3. **Solution Slide** — Architecture or flow diagram
4. **Demo Slides** — Screenshots with annotations
5. **Metrics Slide** — Big numbers with context
6. **Roadmap Slide** — What's done, what's next
7. **Ask Slide** — Clear request + next steps

---

## PowerPoint Generation

```bash
# Install dependencies
pip install python-pptx Pillow

# Generate PPTX (basic)
python scripts/generate_pptx.py --output demo.pptx

# Generate with screenshots
python scripts/generate_pptx.py --output demo.pptx --screenshots ./screenshots

# Generate with iceberg palette
python scripts/generate_pptx.py --output demo.pptx --palette iceberg
```

### PPTX Features

- **10-slide structure** with iceberg visualization for problem slides
- **Color palettes:** `default` (blue/gray) or `iceberg` (sky/ocean)
- **Screenshot integration:** Auto-detects images in screenshots folder
- **Speaker notes:** Timing and talking points for each slide

See `scripts/generate_pptx.py` for customization options.

---

## Terminal Demo Script

The `templates/demo.sh` script provides a modular terminal-based demo:

```bash
# Run full demo
./templates/demo.sh

# Run specific sections
./templates/demo.sh 1 2 3      # Sections 1, 2, 3 only
./templates/demo.sh 3          # Just the live demo section
```

### Sections

| Section | Name | Content |
|---------|------|---------|
| 0 | Title | ASCII art title card |
| 1 | Hook | Problem statement |
| 2 | Solution | Architecture overview |
| 3 | Demo | Live demo (API calls, interactive) |
| 4 | Results | Metrics and validation |
| 5 | Next | Challenges and roadmap |
| 6 | Ask | Clear ask and closing |

Features:
- Color-coded output
- Pause between sections for presenter control
- Optional live API calls
- Server health checks

---

## Files Structure

```
demo-prep-skill/
├── SKILL.md                   # This file
├── README.md                  # Quick start guide
├── templates/
│   ├── interactive.html       # HTML presentation with timer
│   ├── script.md              # Technical demo script
│   ├── script-csuite.md       # C-Suite focused script
│   └── demo.sh                # Terminal demo (bash)
├── scripts/
│   └── generate_pptx.py       # PowerPoint generator (10 slides)
├── screenshots/               # Add your screenshots here
│   └── .gitkeep
└── examples/
    └── .gitkeep               # Your customized demos
```
