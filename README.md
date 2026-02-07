# Demo Prep Skill

A Claude Code skill for preparing product demos — from technical walkthroughs to C-suite presentations.

## Features

- **Interactive HTML Presentation** — McKinsey-style slides with architecture pipelines, iceberg visualizations, and score factor panels
- **Terminal Demo Script** — Modular bash script for terminal-based demos with live API calls
- **PowerPoint Generator** — 10-slide presentations with color palettes and screenshot integration
- **Dual Script Templates** — Technical and C-Suite focused presenter scripts
- **Timer Presets** — 3, 5, 7 minute presets + custom duration
- **Live API Support** — Execute real-time API calls during demos

## What's Included

| File | Purpose |
|------|---------|
| `SKILL.md` | Skill definition with demo frameworks and best practices |
| `templates/interactive.html` | McKinsey-style HTML presentation with timer |
| `templates/script.md` | Technical presenter script with timing markers |
| `templates/script-csuite.md` | Executive-focused script with objection handling |
| `templates/demo.sh` | Terminal demo script (modular, color-coded) |
| `scripts/generate_pptx.py` | PowerPoint generator (10 slides, palettes, screenshots) |

## Installation

### Option 1: Add to an existing Claude Code project

Copy the skill files into your project's root directory:

```bash
# Clone the repo
git clone https://github.com/MohamedBIqbal/demo-prep-skill.git

# Copy files to your project
cp demo-prep-skill/SKILL.md /path/to/your/project/DEMO_SKILL.md
cp -r demo-prep-skill/templates /path/to/your/project/demo/
cp -r demo-prep-skill/scripts /path/to/your/project/demo/
```

Or add as a git submodule:
```bash
cd /path/to/your/project
git submodule add https://github.com/MohamedBIqbal/demo-prep-skill.git skills/demo-prep
```

### Option 2: Use as standalone project
```bash
git clone https://github.com/MohamedBIqbal/demo-prep-skill.git
cd demo-prep-skill
```

### Option 3: Reference in CLAUDE.md

Add to your project's `CLAUDE.md`:
```markdown
## Demo Preparation

When preparing demos, reference the frameworks in `skills/demo-prep/SKILL.md`:
- Use McKinsey Pyramid Principle (Answer → Proof → Details)
- Follow 5-minute structure: Hook → Solution → Demo → Results → Ask
- Use built-in timer (T key) during practice runs
```

## Usage

In Claude Code, ask:
```
> Help me prepare a 5-minute demo for [your product]
> Create presentation slides for my API demo
> I need a C-suite pitch for [product]
```

Claude will use the frameworks in SKILL.md to help you:
1. Structure your demo (Hook → Solution → Demo → Results → Ask)
2. Customize the HTML template for your product
3. Generate a PowerPoint presentation

## Demo Frameworks

### Technical Demo (5 min)
| Segment | Duration | Content |
|---------|----------|---------|
| Hook + Problem | 1 min | Why this matters |
| Solution | 30 sec | Architecture overview |
| Live Demo | 2 min | Show it working |
| Results | 30 sec | Metrics, proof |
| The Ask | 30 sec | What you need |

### C-Suite Format
- Lead with the answer (Pyramid Principle)
- 30% talking / 40% showing / 30% discussion
- End with a clear, specific ask

## Customizing the Template

1. Open `templates/interactive.html`
2. Replace placeholder content with your product info
3. Connect to your API (if applicable)
4. Run in browser or generate PPTX

### Built-in Presentation Timer

The HTML template includes a configurable timer to keep your demo on track:

| Preset | Use Case |
|--------|----------|
| 3 min | Lightning talk, elevator pitch |
| 5 min | Standard demo (default) |
| 7 min | Extended demo with Q&A buffer |
| Custom | Set any duration (1-30 min) |

**Keyboard shortcuts:**
- `T` — Open timer configuration
- `S` — Start/stop timer
- `N` — Toggle speaker notes
- `←` `→` — Navigate slides

**Visual alerts:** Timer turns amber at 2 min remaining, red at 1 min.

### Live API Execution

The template supports real-time API calls during your demo. Connect to any backend to show live data:

```javascript
// Replace with your API base URL
const API_BASE = "http://localhost:8000";

// Replace with your endpoints
async function runDemo() {
    const response = await fetch(`${API_BASE}/your-endpoint`);
    const data = await response.json();
    // Display results in your demo
    document.getElementById('demoOutput').innerHTML = formatResults(data);
}
```

This allows you to:
- Query your API live during the presentation
- Show real responses, not screenshots
- Demonstrate actual product behavior

## Generating PowerPoint

```bash
# Install dependencies
pip install python-pptx Pillow

# Generate PPTX (basic)
python scripts/generate_pptx.py --output my_demo.pptx

# Generate with screenshots (auto-detected from folder)
python scripts/generate_pptx.py --output my_demo.pptx --screenshots ./screenshots

# Generate with iceberg color palette
python scripts/generate_pptx.py --output my_demo.pptx --palette iceberg
```

### PPTX Features

- **10-slide structure** with iceberg visualization for problem slides
- **Story-based color palettes:**
  - `default` — Corporate professional (blue/gray)
  - `iceberg` — Hidden costs narrative (sky above, ocean below)
- **Screenshot integration:** Auto-detects images in screenshots folder (4.png, 5.png, etc.)
- **Speaker notes:** Timing and talking points for each slide

### Iceberg Storytelling Theme

Use `--palette iceberg` when your demo reveals hidden costs or "tip of the iceberg" problems:

```bash
python scripts/generate_pptx.py --output demo.pptx --palette iceberg
```

The iceberg visualization shows visible costs above the waterline and hidden damage below — a powerful metaphor for compliance, security, or cost-focused demos.

## Terminal Demo

Run demos directly in the terminal:

```bash
# Full demo
./templates/demo.sh

# Specific sections only
./templates/demo.sh 1 2 3    # Sections 1, 2, 3
./templates/demo.sh 3        # Just the live demo
```

Sections: 0=title, 1=hook, 2=solution, 3=demo, 4=results, 5=next, 6=ask

## Requirements

- Python 3.8+ (for PPTX generation)
- python-pptx
- Pillow
- Modern browser (for HTML presentation)

## Examples

See the `examples/` folder for real-world implementations.

## License

MIT License - see [LICENSE](LICENSE)

## Credits

Built with Claude Code. Inspired by McKinsey presentation methodology.
