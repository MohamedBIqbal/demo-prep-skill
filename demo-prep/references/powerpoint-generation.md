# PowerPoint Generation

## When to Generate PPTX

Use PPTX when you need:
- Shareable offline deck (no API/internet required)
- Corporate template compliance
- Leave-behind for stakeholders
- Backup if live demo fails

## Quick Generate Command

```bash
# Requires: pip install python-pptx Pillow
python scripts/generate_pptx.py interactive.html output.pptx
```

## PPTX Structure (Pyramid Principle)

| Slide | Content | Design |
|-------|---------|--------|
| 1. Title | Product name + one-line value prop + ask | Bold title, minimal text |
| 2. Problem | The gap / pain point | Visual contrast (red/amber) |
| 3. Solution | Architecture overview | Pipeline diagram |
| 4. Demo Screenshots | Key screens from live demo | Annotated images |
| 5. Proof | Metrics, test results, scores | Charts/numbers |
| 6. Next Steps | Clear ask + timeline | Action-oriented |

## Slide Design Guidelines

### Typography
- **Title:** 36-44pt, bold
- **Subtitle:** 24-28pt
- **Body:** 18-20pt
- **Max 6 words per bullet**
- **Max 6 bullets per slide**

### Colors (Corporate-Safe Palette)
```python
COLORS = {
    'primary': '0066CC',      # Blue - headers, emphasis
    'secondary': '2D3748',    # Dark gray - body text
    'accent': '10B981',       # Green - success, metrics
    'warning': 'F59E0B',      # Amber - caution, judge
    'danger': 'DC2626',       # Red - risk, problems
    'background': 'FFFFFF',   # White
    'light_bg': 'F8FAFC',     # Light gray - cards
}
```

### Layout Templates
1. **Title Slide** - Centered, logo optional
2. **Section Header** - Full-width color band
3. **Content + Visual** - 60/40 split
4. **Comparison** - Two columns (green vs red)
5. **Pipeline/Flow** - Horizontal stages
6. **Metrics** - Big numbers with labels
7. **Screenshot** - Full-bleed image with caption

## HTML to PPTX Mapping

| HTML Element | PPTX Equivalent |
|--------------|-----------------|
| `.slide` div | New slide |
| `.action-title` | Slide title |
| `.context` | Subtitle/header |
| `.arch-pipeline` | SmartArt or shapes |
| `.callout-item` | Bullet points |
| Screenshots | `add_picture()` |

## Python-PPTX Quick Reference

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RgbColor
from pptx.enum.text import PP_ALIGN

# Create presentation
prs = Presentation()
prs.slide_width = Inches(13.333)  # 16:9
prs.slide_height = Inches(7.5)

# Add slide
slide_layout = prs.slide_layouts[6]  # Blank
slide = prs.slides.add_slide(slide_layout)

# Add title
title = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12), Inches(1))
tf = title.text_frame
tf.paragraphs[0].text = "Slide Title"
tf.paragraphs[0].font.size = Pt(40)
tf.paragraphs[0].font.bold = True

# Add shape
shape = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(1), Inches(2), Inches(2), Inches(1)
)
shape.fill.solid()
shape.fill.fore_color.rgb = RgbColor(0x00, 0x66, 0xCC)

# Save
prs.save('output.pptx')
```

## Generating from Live Demo

1. **Take screenshots** of key slides from `interactive.html`
2. **Extract content** (titles, bullets, metrics)
3. **Generate PPTX** with matching structure
4. **Add speaker notes** from `script.md`

```bash
# Capture screenshots (requires playwright)
python scripts/capture_screenshots.py http://localhost:8080/interactive.html

# Generate PPTX from screenshots + content
python scripts/generate_pptx.py --screenshots ./captures --output demo.pptx
```

## Speaker Notes Template

Each slide should have notes in this format:
```
TIMING: [duration]
SAY: [exact words]
SHOW: [what to point at]
TRANSITION: [how to move to next slide]
```

---

## Files in This Folder

| File | Purpose |
|------|---------|
| `interactive.html` | Main interactive presentation with live API calls |
| `slides.html` | Simple static HTML slides (backup) |
| `script.md` | Original technical presenter script |
| `script-csuite.md` | C-suite optimized presenter script |
| `demo.sh` | Terminal demo with section-by-section execution |
| `scripts/generate_pptx.py` | Generate PPTX from HTML demo |
| `scripts/capture_screenshots.py` | Capture slide screenshots |

---

## Resources

- [anthropics/skills/web-artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder)
