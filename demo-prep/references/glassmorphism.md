# Glassmorphism Presentation Design

## When to Use

Use glassmorphism for high-impact presentation slides when you need:
- Visual "wow factor" for demos and pitches
- Modern, premium aesthetic
- Layered information architecture
- Content that pops against dynamic backgrounds

---

## Core Glassmorphism CSS

### The Glass Effect

```css
.glass-card {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.4);
  border-radius: 24px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}
```

### Animated Gradient Background

```css
@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.animated-bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(-45deg, #0071e3, #5856d6, #af52de, #ff9500, #34c759, #0071e3);
  background-size: 400% 400%;
  animation: gradientShift 15s ease infinite;
}
```

### Floating Animation

```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}

.floating-card {
  animation: float 4s ease-in-out infinite;
}

/* Stagger animation delay for multiple cards */
.card-1 { animation-delay: 0s; }
.card-2 { animation-delay: 0.5s; }
.card-3 { animation-delay: 1s; }
.card-4 { animation-delay: 1.5s; }
```

---

## Layered Compliance Slide Pattern

For showing stacked frameworks/layers (like compliance):

### Structure

```
┌─────────────────────────────────────────┐
│ [Icon] LAYER 1 TITLE                    │ ← Glass card
│ Subtitle / description                  │
│ [Pills/badges showing items]            │
└─────────────────────────────────────────┘
                    │
                    ▼ (Connector)
┌─────────────────────────────────────────┐
│ [Icon] LAYER 2 TITLE                    │
│ ...                                     │
└─────────────────────────────────────────┘
```

### Connector Element

```css
.connector {
  width: 3px;
  height: 28px;
  background: linear-gradient(180deg, rgba(255,255,255,0.8) 0%, rgba(255,255,255,0.3) 100%);
  margin: 0 auto;
  border-radius: 2px;
  position: relative;
}

.connector::after {
  content: '▼';
  position: absolute;
  bottom: -12px;
  left: 50%;
  transform: translateX(-50%);
  color: rgba(255,255,255,0.8);
  font-size: 10px;
}
```

### Icon Badges (Gradient)

```css
.icon-badge {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

/* Color variants */
.icon-green { background: linear-gradient(135deg, #34c759 0%, #30d158 100%); }
.icon-blue { background: linear-gradient(135deg, #0071e3 0%, #5856d6 100%); }
.icon-orange { background: linear-gradient(135deg, #ff9500 0%, #ff6b00 100%); }
.icon-purple { background: linear-gradient(135deg, #af52de 0%, #8944ab 100%); }
```

### Pill Badges

```css
.pill {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 20px;
  font-size: 10px;
  font-weight: 600;
  margin: 2px;
}

/* Colored pill variants */
.pill-blue {
  background: rgba(0, 113, 227, 0.1);
  color: #0071e3;
}

.pill-orange {
  background: rgba(255, 149, 0, 0.1);
  color: #cc7700;
}

.pill-purple {
  background: rgba(175, 82, 222, 0.1);
  color: #8944ab;
}

.pill-success {
  background: rgba(52, 199, 89, 0.1);
  color: #34c759;
}
```

---

## Complete Glassmorphism Slide Template

```html
<div class="slide">
  <style>
    @keyframes gradientShift {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    @keyframes float {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-8px); }
    }
    .slide-bg {
      position: absolute;
      inset: 0;
      background: linear-gradient(-45deg, #0071e3, #5856d6, #af52de, #ff9500, #34c759, #0071e3);
      background-size: 400% 400%;
      animation: gradientShift 15s ease infinite;
    }
    .glass {
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.4);
      border-radius: 24px;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
  </style>

  <!-- Animated Background -->
  <div class="slide-bg"></div>

  <!-- Content Layer -->
  <div style="position: relative; z-index: 1; padding: 30px 60px;">

    <!-- Header (white text on gradient) -->
    <div style="text-align: center; margin-bottom: 20px;">
      <div style="font-size: 11px; color: rgba(255,255,255,0.9); text-transform: uppercase; letter-spacing: 2px;">
        SECTION LABEL
      </div>
      <h1 style="font-size: 36px; font-weight: 700; color: white; text-shadow: 0 2px 20px rgba(0,0,0,0.2);">
        Main Title Here
      </h1>
    </div>

    <!-- Glass Cards Stack -->
    <div style="display: flex; flex-direction: column; gap: 8px; max-width: 1000px; margin: 0 auto;">

      <!-- Card 1 -->
      <div class="glass" style="padding: 16px 24px; animation: float 4s ease-in-out infinite;">
        <div style="display: flex; align-items: center; gap: 20px;">
          <div style="width: 56px; height: 56px; background: linear-gradient(135deg, #34c759, #30d158); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 28px;">
            👤
          </div>
          <div style="flex: 1;">
            <div style="font-size: 16px; font-weight: 700; color: #1d1d1f;">CARD TITLE</div>
            <div style="font-size: 12px; color: #86868b;">Description text here</div>
          </div>
          <div style="font-size: 11px; color: #34c759; font-weight: 600; background: rgba(52,199,89,0.1); padding: 6px 14px; border-radius: 20px;">
            STATUS
          </div>
        </div>
      </div>

      <!-- Connector -->
      <div style="width: 3px; height: 28px; background: linear-gradient(180deg, rgba(255,255,255,0.8), rgba(255,255,255,0.3)); margin: 0 auto; border-radius: 2px; position: relative;">
        <span style="position: absolute; bottom: -12px; left: 50%; transform: translateX(-50%); color: rgba(255,255,255,0.8); font-size: 10px;">▼</span>
      </div>

      <!-- Card 2 (with pills) -->
      <div class="glass" style="padding: 16px 24px; animation: float 4s ease-in-out infinite 0.5s;">
        <div style="display: flex; align-items: flex-start; gap: 20px;">
          <div style="width: 56px; height: 56px; background: linear-gradient(135deg, #0071e3, #5856d6); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 24px;">
            🤖
          </div>
          <div style="flex: 1;">
            <div style="font-size: 14px; font-weight: 700; color: #1d1d1f; margin-bottom: 8px;">
              CARD TITLE
              <span style="font-size: 10px; color: #86868b; font-weight: 400; margin-left: 8px;">Subtitle</span>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 4px;">
              <span style="background: rgba(0,113,227,0.1); color: #0071e3; padding: 3px 10px; border-radius: 20px; font-size: 10px; font-weight: 600;">✓ Item 1</span>
              <span style="background: rgba(0,113,227,0.1); color: #0071e3; padding: 3px 10px; border-radius: 20px; font-size: 10px; font-weight: 600;">✓ Item 2</span>
              <span style="background: rgba(0,113,227,0.1); color: #0071e3; padding: 3px 10px; border-radius: 20px; font-size: 10px; font-weight: 600;">✓ Item 3</span>
            </div>
          </div>
          <div style="font-size: 18px; font-weight: 700; color: #34c759;">10/10</div>
        </div>
      </div>

    </div>
  </div>
</div>
```

---

## Design Tips

### Do's
- Use subtle transparency (0.8-0.9 for light backgrounds)
- Match blur to content density (20px for cards, 10px for overlays)
- Stagger floating animations by 0.5s increments
- Use gradient backgrounds with 5-6 color stops for smooth transitions
- Add subtle white borders (1px, 0.4 opacity) for depth

### Don'ts
- Don't use glassmorphism on large areas (GPU-intensive)
- Don't stack more than 2 glass layers
- Don't use with low-contrast text
- Don't animate blur values (causes jank)
- Don't use on text-heavy slides

### Accessibility
- Ensure 4.5:1 contrast ratio for text on glass
- Test with backdrop-filter disabled (fallback solid background)
- Don't rely solely on color for meaning
- Keep animations under 5s or provide reduced-motion alternative

---

## Color Palette for Compliance Slides

| Framework | Primary | Gradient | Icon |
|-----------|---------|----------|------|
| Human in Loop | #34c759 | #34c759 → #30d158 | 👤 |
| AI Guidelines | #0071e3 | #0071e3 → #5856d6 | 🤖 |
| ALCOA+ | #ff9500 | #ff9500 → #ff6b00 | 📋 |
| 21 CFR Part 11 | #af52de | #af52de → #8944ab | 🔐 |
| Success/Check | #34c759 | — | ✓ |

---
