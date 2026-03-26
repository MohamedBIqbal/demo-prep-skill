# Apple Style UI Prep

## Design Philosophy

Apple's UI approach centers on **clarity**, **deference**, and **depth**. The interface should feel inevitable—like no other design was possible.

### Core Principles

| Principle | What It Means |
|-----------|---------------|
| **Clarity** | Text is legible, icons are precise, ornament is purposeful |
| **Deference** | UI gets out of the way—content is the star |
| **Depth** | Subtle layers, realistic motion, meaningful transitions |

---

## Typography

### SF Pro (Apple's System Font)

```css
font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', sans-serif;
```

### Hierarchy

| Level | Size | Weight | Use Case |
|-------|------|--------|----------|
| Large Title | 34px | Bold (700) | Page headers |
| Title 1 | 28px | Bold (700) | Section headers |
| Title 2 | 22px | Bold (700) | Card titles |
| Title 3 | 20px | Semibold (600) | Subsections |
| Headline | 17px | Semibold (600) | Emphasized body |
| Body | 17px | Regular (400) | Primary content |
| Callout | 16px | Regular (400) | Secondary content |
| Subhead | 15px | Regular (400) | Supporting text |
| Footnote | 13px | Regular (400) | Captions, labels |
| Caption | 12px | Regular (400) | Timestamps, metadata |

### Letter Spacing

- **Headings:** -0.5px to -1px (tighter)
- **Body:** 0 to -0.2px (subtle)
- **Small text:** +0.2px (slightly looser for legibility)

---

## Color Palette

### System Colors

```css
:root {
  /* Primary */
  --apple-blue: #007AFF;
  --apple-green: #34C759;
  --apple-orange: #FF9500;
  --apple-red: #FF3B30;
  --apple-purple: #AF52DE;
  --apple-pink: #FF2D55;
  --apple-teal: #5AC8FA;
  --apple-yellow: #FFCC00;

  /* Grayscale */
  --gray-1: #8E8E93;
  --gray-2: #AEAEB2;
  --gray-3: #C7C7CC;
  --gray-4: #D1D1D6;
  --gray-5: #E5E5EA;
  --gray-6: #F2F2F7;

  /* Backgrounds */
  --bg-primary: #FFFFFF;
  --bg-secondary: #F2F2F7;
  --bg-tertiary: #FFFFFF;

  /* Text */
  --text-primary: #000000;
  --text-secondary: #3C3C43; /* 60% opacity */
  --text-tertiary: #3C3C43;  /* 30% opacity */
}
```

### Dark Mode

```css
@media (prefers-color-scheme: dark) {
  :root {
    --bg-primary: #000000;
    --bg-secondary: #1C1C1E;
    --bg-tertiary: #2C2C2E;
    --text-primary: #FFFFFF;
    --text-secondary: rgba(235, 235, 245, 0.6);
  }
}
```

---

## Spacing & Layout

### 8-Point Grid

All spacing uses multiples of 8px:

| Token | Value | Use Case |
|-------|-------|----------|
| `xs` | 4px | Tight internal spacing |
| `sm` | 8px | Related elements |
| `md` | 16px | Section padding |
| `lg` | 24px | Card padding |
| `xl` | 32px | Section gaps |
| `2xl` | 48px | Major divisions |
| `3xl` | 64px | Page margins |

### Content Width

```css
.container {
  max-width: 980px;      /* Content */
  max-width: 1200px;     /* Wide layouts */
  padding: 0 20px;       /* Mobile safe area */
}
```

### Card Anatomy

```css
.apple-card {
  background: var(--bg-tertiary);
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}
```

---

## Components

### Buttons

```css
/* Primary (filled) */
.btn-primary {
  background: var(--apple-blue);
  color: white;
  border-radius: 12px;
  padding: 12px 24px;
  font-weight: 600;
  font-size: 17px;
  border: none;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.btn-primary:hover {
  opacity: 0.85;
}

/* Secondary (outline) */
.btn-secondary {
  background: transparent;
  color: var(--apple-blue);
  border: 1px solid var(--apple-blue);
  border-radius: 12px;
  padding: 12px 24px;
}

/* Text button */
.btn-text {
  background: none;
  border: none;
  color: var(--apple-blue);
  font-weight: 600;
  cursor: pointer;
}
```

### Input Fields

```css
.input-field {
  background: var(--gray-6);
  border: none;
  border-radius: 10px;
  padding: 12px 16px;
  font-size: 17px;
  width: 100%;
  transition: background 0.2s ease;
}

.input-field:focus {
  outline: none;
  background: var(--gray-5);
  box-shadow: 0 0 0 4px rgba(0, 122, 255, 0.2);
}
```

### Segmented Control

```css
.segmented-control {
  display: inline-flex;
  background: var(--gray-6);
  border-radius: 8px;
  padding: 2px;
}

.segment {
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.segment.active {
  background: white;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}
```

### Lists

```css
.list-item {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  border-bottom: 0.5px solid var(--gray-4);
}

.list-item:last-child {
  border-bottom: none;
}

.list-item .chevron {
  color: var(--gray-3);
  margin-left: auto;
}
```

---

## Motion & Animation

### Timing Functions

```css
/* Apple's custom easing */
--ease-in-out-apple: cubic-bezier(0.4, 0, 0.2, 1);
--ease-out-apple: cubic-bezier(0, 0, 0.2, 1);
--ease-in-apple: cubic-bezier(0.4, 0, 1, 1);

/* Spring-like */
--spring: cubic-bezier(0.175, 0.885, 0.32, 1.275);
```

### Durations

| Type | Duration | Use Case |
|------|----------|----------|
| Micro | 100ms | Button press feedback |
| Fast | 200ms | Toggle, small state changes |
| Normal | 300ms | Modals, sheets, transitions |
| Slow | 500ms | Page transitions, reveals |

### Common Animations

```css
/* Fade in */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Scale in (modal) */
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Slide up (sheet) */
@keyframes slideUp {
  from {
    transform: translateY(100%);
  }
  to {
    transform: translateY(0);
  }
}
```

---

## Vibrancy & Materials

### Frosted Glass Effect

```css
.frosted {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
}

/* Dark mode */
.frosted-dark {
  background: rgba(30, 30, 30, 0.7);
  backdrop-filter: blur(20px);
}
```

### Shadows (Elevation)

```css
/* Subtle */
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);

/* Card */
--shadow-md: 0 4px 12px rgba(0, 0, 0, 0.08);

/* Modal */
--shadow-lg: 0 10px 40px rgba(0, 0, 0, 0.12);

/* Floating */
--shadow-xl: 0 20px 60px rgba(0, 0, 0, 0.2);
```

---

## Icons

### SF Symbols Guidelines

- Use SF Symbols when possible (or similar outline icons)
- Weight should match nearby text weight
- Sizes: 17pt (inline), 22pt (nav), 28pt (feature)
- Use template rendering (single color inherits text color)

### Icon Sizing

| Context | Size | Padding |
|---------|------|---------|
| Inline with text | 17-20px | 0 |
| Navigation bar | 22-24px | 12px tap target |
| Tab bar | 24-28px | 44px min tap |
| Feature icon | 28-44px | 16px+ |

---

## Layout Patterns

### Navigation Bar

```css
.navbar {
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-bottom: 0.5px solid var(--gray-4);
}

.navbar-title {
  font-size: 17px;
  font-weight: 600;
}
```

### Tab Bar

```css
.tab-bar {
  display: flex;
  justify-content: space-around;
  height: 49px;
  padding-bottom: env(safe-area-inset-bottom);
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-top: 0.5px solid var(--gray-4);
}

.tab-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 10px;
  color: var(--gray-1);
}

.tab-item.active {
  color: var(--apple-blue);
}
```

### Modal / Sheet

```css
.modal {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: white;
  border-radius: 12px 12px 0 0;
  padding: 20px;
  padding-bottom: calc(20px + env(safe-area-inset-bottom));
  animation: slideUp 0.3s var(--ease-out-apple);
}

.modal-handle {
  width: 36px;
  height: 5px;
  background: var(--gray-4);
  border-radius: 3px;
  margin: 0 auto 12px;
}
```

---

## Responsive Breakpoints

```css
/* Compact (iPhone) */
@media (max-width: 428px) { }

/* Regular (iPad Portrait) */
@media (min-width: 429px) and (max-width: 768px) { }

/* Regular Wide (iPad Landscape) */
@media (min-width: 769px) and (max-width: 1024px) { }

/* Full (Desktop) */
@media (min-width: 1025px) { }
```

---

## Checklist: Apple Style UI

### Visual
- [ ] Using SF Pro or system font stack
- [ ] 8-point grid spacing
- [ ] Rounded corners (10-12px for cards, 8px for buttons)
- [ ] Subtle shadows, no harsh borders
- [ ] White space is generous

### Typography
- [ ] Limited font sizes (use hierarchy table)
- [ ] Tight letter-spacing on headings
- [ ] No more than 2-3 font weights per screen

### Color
- [ ] Mostly grayscale with one accent color
- [ ] Color conveys meaning (blue = action, red = destructive)
- [ ] Dark mode support

### Motion
- [ ] Smooth easing (no linear)
- [ ] Quick, purposeful animations (200-300ms)
- [ ] No gratuitous movement

### Interaction
- [ ] 44px minimum tap targets
- [ ] Immediate visual feedback on press
- [ ] Clear focus states

---

## Quick Start Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Apple Style UI</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif;
      background: #F2F2F7;
      color: #000;
      line-height: 1.4;
      -webkit-font-smoothing: antialiased;
    }

    .container {
      max-width: 980px;
      margin: 0 auto;
      padding: 48px 20px;
    }

    .card {
      background: white;
      border-radius: 12px;
      padding: 20px;
      margin-bottom: 16px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    h1 {
      font-size: 34px;
      font-weight: 700;
      letter-spacing: -0.5px;
      margin-bottom: 24px;
    }

    .btn {
      background: #007AFF;
      color: white;
      border: none;
      border-radius: 12px;
      padding: 12px 24px;
      font-size: 17px;
      font-weight: 600;
      cursor: pointer;
      transition: opacity 0.2s ease;
    }

    .btn:hover {
      opacity: 0.85;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Your App Title</h1>
    <div class="card">
      <p>Content goes here</p>
    </div>
    <button class="btn">Get Started</button>
  </div>
</body>
</html>
```
