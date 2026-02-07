#!/usr/bin/env python3
"""
Generate McKinsey-style PowerPoint Presentation

A template script for creating professional demo presentations.
Customize the slide content to match your product.

Usage:
    python generate_pptx.py --output my_demo.pptx

Requires:
    pip install python-pptx Pillow
"""

import argparse
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor


# ============ COLOR PALETTE ============
# Corporate-safe colors that work in any context
COLORS = {
    'primary': RGBColor(0x00, 0x66, 0xCC),       # Blue - headers, emphasis
    'primary_dark': RGBColor(0x00, 0x52, 0xA3),  # Dark blue
    'secondary': RGBColor(0x1E, 0x29, 0x3B),     # Dark gray - body text
    'accent': RGBColor(0x10, 0xB9, 0x81),        # Green - success
    'warning': RGBColor(0xD9, 0x77, 0x06),       # Amber - caution
    'danger': RGBColor(0xDC, 0x26, 0x26),        # Red - risks
    'purple': RGBColor(0x8B, 0x5C, 0xF6),        # Purple - accent
    'white': RGBColor(0xFF, 0xFF, 0xFF),
    'light_gray': RGBColor(0xF8, 0xFA, 0xFC),    # Background
    'muted': RGBColor(0x64, 0x74, 0x8B),         # Muted text
    'border': RGBColor(0xE2, 0xE8, 0xF0),        # Border
}


# ============ HELPER FUNCTIONS ============

def add_context_label(slide, text, color=None):
    """Add context label at top of slide (e.g., 'THE PROBLEM')"""
    ctx = slide.shapes.add_textbox(Inches(0.75), Inches(0.6), Inches(3), Inches(0.4))
    tf = ctx.text_frame
    p = tf.paragraphs[0]
    p.text = text.upper()
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = color or COLORS['primary']
    return ctx


def add_action_title(slide, text, y=1.0):
    """Add McKinsey action title - the takeaway, not a topic label"""
    title_box = slide.shapes.add_textbox(Inches(0.75), Inches(y), Inches(11.8), Inches(1.2))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = COLORS['secondary']
    p.line_spacing = 1.2
    return title_box


def add_card(slide, x, y, width, height, title, content, title_color=None, border_color=None):
    """Add a card with title and content"""
    card = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(x), Inches(y), Inches(width), Inches(height)
    )
    card.fill.solid()
    card.fill.fore_color.rgb = COLORS['white']
    card.line.color.rgb = border_color or COLORS['border']
    card.line.width = Pt(1)

    # Title
    title_box = slide.shapes.add_textbox(
        Inches(x + 0.2), Inches(y + 0.2), Inches(width - 0.4), Inches(0.5)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = title_color or COLORS['primary']

    # Content
    content_box = slide.shapes.add_textbox(
        Inches(x + 0.2), Inches(y + 0.6), Inches(width - 0.4), Inches(height - 0.8)
    )
    tf = content_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = content
    p.font.size = Pt(12)
    p.font.color.rgb = COLORS['muted']
    p.line_spacing = 1.4

    return card


def add_speaker_notes(slide, text):
    """Add speaker notes to slide"""
    notes = slide.notes_slide
    notes.notes_text_frame.text = text


# ============ SLIDE BUILDERS ============
# Customize these functions with your content

def slide_1_title(prs, config):
    """Slide 1: Title - Your product and value prop"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # Main message
    title_box = slide.shapes.add_textbox(Inches(0.75), Inches(2), Inches(8), Inches(2))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = config.get('product_name', 'Your Product Name')
    p.font.size = Pt(48)
    p.font.bold = True
    p.font.color.rgb = COLORS['primary']

    p = tf.add_paragraph()
    p.text = config.get('tagline', 'One-sentence value proposition')
    p.font.size = Pt(24)
    p.font.color.rgb = COLORS['muted']

    # Feature cards at bottom
    features = config.get('features', [
        ('Feature 1', 'Brief description'),
        ('Feature 2', 'Brief description'),
        ('Feature 3', 'Brief description'),
    ])
    card_x = 0.75
    for title, desc in features:
        add_card(slide, card_x, 5.0, 3.6, 1.5, title, desc)
        card_x += 3.9

    add_speaker_notes(slide, """TIMING: 30 seconds
SAY: State your one-line value prop
TRANSITION: "Here's the problem we're solving..." """)

    return slide


def slide_2_problem(prs, config):
    """Slide 2: The Problem"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    add_context_label(slide, "The Problem", COLORS['danger'])
    add_action_title(slide, config.get('problem_title', 'State the problem as an action title'))

    # Pain points
    pain_points = config.get('pain_points', ['Pain point 1', 'Pain point 2', 'Pain point 3'])
    y = 2.8
    for point in pain_points:
        box = slide.shapes.add_textbox(Inches(0.75), Inches(y), Inches(5), Inches(0.4))
        tf = box.text_frame
        p = tf.paragraphs[0]
        p.text = f"❌  {point}"
        p.font.size = Pt(16)
        p.font.color.rgb = COLORS['secondary']
        y += 0.5

    # Risk box
    risk_shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(6.5), Inches(2.5), Inches(5.5), Inches(3)
    )
    risk_shape.fill.solid()
    risk_shape.fill.fore_color.rgb = RGBColor(0xFE, 0xE2, 0xE2)
    risk_shape.line.color.rgb = COLORS['danger']
    risk_shape.line.width = Pt(2)

    risk_title = slide.shapes.add_textbox(Inches(6.8), Inches(2.8), Inches(5), Inches(0.5))
    tf = risk_title.text_frame
    p = tf.paragraphs[0]
    p.text = "⚠️  THE RISK"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLORS['danger']

    risk_text = slide.shapes.add_textbox(Inches(6.8), Inches(3.4), Inches(5), Inches(1.5))
    tf = risk_text.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = config.get('risk_text', 'What happens if this problem isn\'t solved?')
    p.font.size = Pt(16)
    p.font.color.rgb = COLORS['secondary']
    p.line_spacing = 1.5

    add_speaker_notes(slide, """TIMING: 45 seconds
SAY: Make them feel the pain
TRANSITION: "Here's the scale..." """)

    return slide


def slide_3_scale(prs, config):
    """Slide 3: Scale / Big Numbers"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    add_context_label(slide, "The Scale")
    add_action_title(slide, config.get('scale_title', 'Big number that shows the magnitude'))

    # Stat cards
    stats = config.get('stats', [
        ('100+', 'metric 1', COLORS['primary'], True),
        ('50K', 'metric 2', COLORS['accent'], False),
        ('99%', 'metric 3', COLORS['purple'], False),
    ])

    card_width = 3.7
    card_x = 0.75
    for value, label, color, is_filled in stats:
        card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(card_x), Inches(2.8), Inches(card_width), Inches(2.2)
        )
        card.fill.solid()
        if is_filled:
            card.fill.fore_color.rgb = color
            card.line.fill.background()
            text_color = COLORS['white']
            label_color = RGBColor(0xA0, 0xC4, 0xE8)
        else:
            card.fill.fore_color.rgb = COLORS['white']
            card.line.color.rgb = COLORS['border']
            card.line.width = Pt(2)
            text_color = color
            label_color = COLORS['muted']

        # Value
        num_box = slide.shapes.add_textbox(Inches(card_x), Inches(3.2), Inches(card_width), Inches(1))
        tf = num_box.text_frame
        p = tf.paragraphs[0]
        p.text = value
        p.font.size = Pt(56)
        p.font.bold = True
        p.font.color.rgb = text_color
        p.alignment = PP_ALIGN.CENTER

        # Label
        label_box = slide.shapes.add_textbox(Inches(card_x), Inches(4.3), Inches(card_width), Inches(0.5))
        tf = label_box.text_frame
        p = tf.paragraphs[0]
        p.text = label
        p.font.size = Pt(14)
        p.font.color.rgb = label_color
        p.alignment = PP_ALIGN.CENTER

        card_x += card_width + 0.3

    add_speaker_notes(slide, """TIMING: 30 seconds
SAY: Show the magnitude of the problem or your solution
TRANSITION: "Here's how it works..." """)

    return slide


def slide_4_solution(prs, config):
    """Slide 4: Solution / Architecture"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    add_context_label(slide, "The Solution")
    add_action_title(slide, config.get('solution_title', 'How your product solves the problem'))

    # Simple flow diagram
    stages = config.get('flow_stages', ['Input', 'Your Product', 'Output'])
    stage_x = 2.0
    for i, stage in enumerate(stages):
        is_main = i == len(stages) // 2  # Middle stage is highlighted

        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(stage_x), Inches(3.5), Inches(2.5), Inches(1.2)
        )
        shape.fill.solid()
        if is_main:
            shape.fill.fore_color.rgb = COLORS['primary']
            shape.line.fill.background()
            text_color = COLORS['white']
        else:
            shape.fill.fore_color.rgb = COLORS['light_gray']
            shape.line.color.rgb = COLORS['border']
            text_color = COLORS['secondary']

        tf = shape.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = stage
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = text_color
        p.alignment = PP_ALIGN.CENTER
        tf.anchor = MSO_ANCHOR.MIDDLE

        # Arrow (except after last)
        if i < len(stages) - 1:
            arrow = slide.shapes.add_textbox(Inches(stage_x + 2.7), Inches(3.8), Inches(0.5), Inches(0.5))
            tf = arrow.text_frame
            p = tf.paragraphs[0]
            p.text = "→"
            p.font.size = Pt(28)
            p.font.color.rgb = COLORS['muted']

        stage_x += 3.2

    add_speaker_notes(slide, """TIMING: 45 seconds
SAY: High-level architecture - don't go too deep
SHOW: Point to each stage
TRANSITION: "Let me show you this working..." """)

    return slide


def slide_5_demo(prs, config):
    """Slide 5: Demo placeholder"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    add_context_label(slide, "Live Demo", COLORS['accent'])
    add_action_title(slide, config.get('demo_title', 'Show, don\'t tell — demonstrate the core value'))

    # Placeholder for screenshot
    placeholder = slide.shapes.add_textbox(Inches(2), Inches(3), Inches(9), Inches(2))
    tf = placeholder.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "📷 Add your demo screenshot here"
    p.font.size = Pt(24)
    p.font.color.rgb = COLORS['muted']
    p.alignment = PP_ALIGN.CENTER

    add_speaker_notes(slide, """TIMING: 2 minutes
SAY: "Watch what happens when..."
SHOW: Run your live demo or show screenshot
TRANSITION: "Here's the proof it works..." """)

    return slide


def slide_6_proof(prs, config):
    """Slide 6: Results / Proof"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    add_context_label(slide, "The Proof", COLORS['accent'])
    add_action_title(slide, config.get('proof_title', 'Metrics and evidence that it works'))

    # Metric cards
    metrics = config.get('metrics', [
        ('95%', 'Metric 1'),
        ('2.5x', 'Metric 2'),
        ('100%', 'Metric 3'),
    ])
    card_x = 0.75
    for value, label in metrics:
        add_card(slide, card_x, 2.8, 3.6, 2.0, f"✓ {label}", "", COLORS['accent'])

        num_box = slide.shapes.add_textbox(Inches(card_x + 0.2), Inches(3.4), Inches(3.2), Inches(0.8))
        tf = num_box.text_frame
        p = tf.paragraphs[0]
        p.text = value
        p.font.size = Pt(36)
        p.font.bold = True
        p.font.color.rgb = COLORS['secondary']

        card_x += 3.9

    add_speaker_notes(slide, """TIMING: 30 seconds
SAY: Back up your claims with numbers
TRANSITION: "Here's the roadmap..." """)

    return slide


def slide_7_roadmap(prs, config):
    """Slide 7: Roadmap + Honest Gaps"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    add_context_label(slide, "Roadmap")
    add_action_title(slide, config.get('roadmap_title', 'What\'s done, what\'s next'))

    # Completed
    completed = config.get('completed', ['Milestone 1', 'Milestone 2', 'Milestone 3'])
    y = 2.8
    for item in completed:
        box = slide.shapes.add_textbox(Inches(0.75), Inches(y), Inches(5), Inches(0.4))
        tf = box.text_frame
        p = tf.paragraphs[0]
        p.text = f"✓  {item}"
        p.font.size = Pt(16)
        p.font.color.rgb = COLORS['accent']
        y += 0.5

    # Gaps
    gaps_shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(6.5), Inches(2.5), Inches(5.5), Inches(3)
    )
    gaps_shape.fill.solid()
    gaps_shape.fill.fore_color.rgb = COLORS['white']
    gaps_shape.line.color.rgb = COLORS['warning']
    gaps_shape.line.width = Pt(2)

    gaps_title = slide.shapes.add_textbox(Inches(6.8), Inches(2.7), Inches(5), Inches(0.5))
    tf = gaps_title.text_frame
    p = tf.paragraphs[0]
    p.text = "⚠️  Honest Gaps"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLORS['warning']

    gaps = config.get('gaps', ['Gap 1', 'Gap 2', 'Gap 3'])
    y = 3.3
    for i, gap in enumerate(gaps, 1):
        box = slide.shapes.add_textbox(Inches(6.8), Inches(y), Inches(5), Inches(0.4))
        tf = box.text_frame
        p = tf.paragraphs[0]
        p.text = f"{i}. {gap}"
        p.font.size = Pt(14)
        p.font.color.rgb = COLORS['muted']
        y += 0.5

    add_speaker_notes(slide, """TIMING: 30 seconds
SAY: Be honest about gaps - it builds trust
TRANSITION: "Here's my ask..." """)

    return slide


def slide_8_ask(prs, config):
    """Slide 8: The Ask"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    add_context_label(slide, "The Ask")
    add_action_title(slide, config.get('ask_title', 'What do you need from the audience?'))

    # Question cards
    add_card(slide, 0.75, 2.5, 5.3, 1.5,
             "💬 Feedback Request",
             config.get('feedback_question', 'What specific feedback do you want?'),
             COLORS['primary'])

    add_card(slide, 6.4, 2.5, 5.3, 1.5,
             "🎯 Priority Question",
             config.get('priority_question', 'What decision do you need help with?'),
             COLORS['warning'])

    # Thank you
    thanks = slide.shapes.add_textbox(Inches(0.75), Inches(5.5), Inches(11.5), Inches(1))
    tf = thanks.text_frame
    p = tf.paragraphs[0]
    p.text = "Thank You"
    p.font.size = Pt(48)
    p.font.bold = True
    p.font.color.rgb = COLORS['primary']
    p.alignment = PP_ALIGN.CENTER

    questions = slide.shapes.add_textbox(Inches(0.75), Inches(6.3), Inches(11.5), Inches(0.5))
    tf = questions.text_frame
    p = tf.paragraphs[0]
    p.text = "Questions?"
    p.font.size = Pt(20)
    p.font.color.rgb = COLORS['muted']
    p.alignment = PP_ALIGN.CENTER

    add_speaker_notes(slide, """TIMING: 30 seconds
SAY: Be specific about what you need
ASK: Open it up for questions
END: Thank them for their time""")

    return slide


# ============ MAIN ============

def generate_presentation(output_path, config=None):
    """Generate the full 8-slide presentation"""
    if config is None:
        config = {}

    prs = Presentation()
    prs.slide_width = Inches(13.333)  # 16:9
    prs.slide_height = Inches(7.5)

    # Build all slides
    slide_1_title(prs, config)
    slide_2_problem(prs, config)
    slide_3_scale(prs, config)
    slide_4_solution(prs, config)
    slide_5_demo(prs, config)
    slide_6_proof(prs, config)
    slide_7_roadmap(prs, config)
    slide_8_ask(prs, config)

    prs.save(output_path)
    print(f"✓ Generated: {output_path}")
    print(f"  8 slides with McKinsey-style formatting")
    print(f"  Add your screenshot to slide 5")


def main():
    parser = argparse.ArgumentParser(description="Generate Demo PPTX")
    parser.add_argument("--output", "-o", default="demo.pptx", help="Output file path")
    args = parser.parse_args()

    # ============ CUSTOMIZE YOUR CONTENT HERE ============
    config = {
        'product_name': 'Your Product',
        'tagline': 'One-sentence value proposition',
        'features': [
            ('Feature 1', 'Brief description'),
            ('Feature 2', 'Brief description'),
            ('Feature 3', 'Brief description'),
        ],
        'problem_title': 'State the problem as an action title',
        'pain_points': ['Pain point 1', 'Pain point 2', 'Pain point 3'],
        'risk_text': 'What happens if this problem isn\'t solved?',
        'scale_title': 'Big number that shows the magnitude',
        'stats': [
            ('100+', 'metric 1', COLORS['primary'], True),
            ('50K', 'metric 2', COLORS['accent'], False),
            ('99%', 'metric 3', COLORS['purple'], False),
        ],
        'solution_title': 'How your product solves the problem',
        'flow_stages': ['Input', 'Your Product', 'Output'],
        'demo_title': 'Show, don\'t tell',
        'proof_title': 'Metrics that prove it works',
        'metrics': [('95%', 'Metric 1'), ('2.5x', 'Metric 2'), ('100%', 'Metric 3')],
        'roadmap_title': 'What\'s done, what\'s next',
        'completed': ['Milestone 1', 'Milestone 2', 'Milestone 3'],
        'gaps': ['Known limitation', 'Future work', 'Open question'],
        'ask_title': 'What do you need from the audience?',
        'feedback_question': 'What specific feedback do you want?',
        'priority_question': 'What decision do you need help with?',
    }

    generate_presentation(args.output, config)


if __name__ == "__main__":
    main()
