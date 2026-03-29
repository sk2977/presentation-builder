# Slide Layout Patterns Reference

Quick reference for CSS patterns used in different slide types. Read this when building the HTML.

## Table of Contents
1. Base slide structure
2. Title/Intro slide
3. Content + Sidebar slide
4. Full-width chart slide
5. Two-chart comparison
6. Matrix/Framework slide
7. Stat boxes
8. Callout/Sidebar box
9. Audience question
10. Progress timeline
11. Data tables
12. Print/PDF CSS

---

## 1. Base Slide Structure

Every slide is a `<section>` with fixed dimensions and CSS Grid:

```css
section.slide {
  width: 1920px;
  height: 1080px;
  max-height: 1080px;
  overflow: hidden;
  display: grid;
  grid-template-columns: 1fr 400px;     /* adjust sidebar width as needed */
  grid-template-rows: auto 1fr auto auto;
  gap: 0 36px;
  padding: 48px 64px 0 64px;
  position: relative;
  background: white;
  page-break-after: always;
}
```

Grid row assignments:
- `.slide-header` -- Row 1, spans both columns
- `.slide-content` -- Row 2, column 1 (uses flexbox internally for vertical fill)
- `.callout-investor` (or any sidebar) -- Row 2, column 2
- `.audience-question` (or bottom element) -- Row 3, spans both columns
- `.timeline-bar` -- Row 4, spans both columns

## 2. Title/Intro Slide

Override the grid with flex for centered content:

```css
section.slide.intro-slide {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  background: linear-gradient(145deg, var(--primary) 0%, [darker-shade] 100%);
  color: white;
  padding: 80px;
  /* Reset grid properties */
  grid-template-columns: none;
  grid-template-rows: none;
  gap: 0;
}
```

Include: brand watermark (large, ~7% opacity), title, subtitle, accent bar, speaker placeholders.

## 3. Content + Sidebar Slide

The default layout. Content in column 1 fills the space, sidebar in column 2:

```html
<section class="slide">
  <div class="slide-header"><!-- title, subtitle --></div>
  <div class="slide-content"><!-- stats, text, charts --></div>
  <div class="callout-sidebar"><!-- investor questions, key stats --></div>
  <div class="bottom-element"><!-- audience question --></div>
  <div class="timeline-bar"><!-- progress nodes --></div>
</section>
```

The `.slide-content` should use `display: flex; flex-direction: column;` so that chart containers with `flex: 1` expand to fill remaining vertical space.

## 4. Full-Width Chart Slide

When the chart IS the slide, drop the sidebar:

```css
section.slide.full-chart {
  grid-template-columns: 1fr;  /* no sidebar */
}
```

## 5. Two-Chart Comparison

Side-by-side charts inside the content area:

```css
.charts-duo {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  flex: 1;
  min-height: 0;
  align-items: center;
}

.charts-duo img {
  width: 100%;
  height: auto;
}
```

## 6. Matrix/Framework Slide

2x2 grid with axis labels:

```css
.matrix-container {
  display: grid;
  grid-template-columns: 48px 1fr 1fr;
  grid-template-rows: auto 1fr 1fr auto;
  gap: 4px;
  flex: 1;
}

/* Y-axis label -- rotated text on the left */
.matrix-ylabel {
  grid-column: 1; grid-row: 2 / 4;
  writing-mode: vertical-lr;
  transform: rotate(180deg);
}

/* X-axis label -- bottom center */
.matrix-xlabel {
  grid-column: 2 / 4; grid-row: 4;
  text-align: center;
}

/* Quadrant cells */
.matrix-cell { padding: 24px 22px; border-radius: 10px; }

/* Color-code quadrants by meaning */
.sweet-spot { background: rgba(green, 0.12); border: 2px solid rgba(green, 0.35); }
.dead-zone  { background: rgba(red, 0.10);   border: 2px solid rgba(red, 0.25); }
.neutral    { background: var(--light-bg);    border: 2px solid #e0e0e0; }
```

## 7. Stat Boxes

Row of key metrics at the top of content slides:

```css
.stats-row { display: flex; gap: 16px; flex-wrap: wrap; }

.stat-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: var(--light-bg);
  border-radius: 10px;
  padding: 14px 28px;
  border-bottom: 3px solid var(--primary);
  min-width: 140px;
}

.stat-box .stat-num { font-size: 34px; font-weight: 700; color: var(--primary); }
.stat-box .stat-label { font-size: 12px; text-transform: uppercase; letter-spacing: 1px; }
```

## 8. Callout/Sidebar Box

Dark-background box for sidebar content:

```css
.callout-sidebar {
  grid-column: 2;
  grid-row: 2;
  background: var(--secondary);  /* dark color */
  border-left: 4px solid var(--accent);
  border-radius: 10px;
  padding: 24px 26px;
  align-self: start;
  color: white;
}

/* Special-colored bullet for emphasis items */
.callout-sidebar li.special {
  color: var(--gold);
  font-weight: 700;
  border-top: 1px solid rgba(255,255,255,0.1);
  padding-top: 12px;
}
```

## 9. Audience Question

Full-width bar at the bottom:

```css
.audience-question {
  grid-column: 1 / -1;
  grid-row: 3;
  background: var(--light-bg);
  border-left: 6px solid var(--primary);
  border-radius: 0 8px 8px 0;
  padding: 14px 24px;
  margin-top: 12px;
}

.audience-question p { font-size: 17px; font-style: italic; }
```

## 10. Progress Timeline

Horizontal dots connected by a line:

```css
.timeline-bar {
  grid-column: 1 / -1;
  grid-row: 4;
  display: flex;
  justify-content: space-between;
  padding: 8px 20px 14px;
  position: relative;
}

/* Connecting line behind the dots */
.timeline-bar::before {
  content: '';
  position: absolute;
  left: 40px; right: 40px; top: 14px;
  height: 2px;
  background: var(--muted);
  opacity: 0.35;
}

.timeline-dot {
  width: 14px; height: 14px;
  border-radius: 50%;
  border: 2.5px solid var(--muted);
  background: white;
}

.timeline-dot.active { background: var(--primary); border-color: var(--primary); }
.timeline-dot.current {
  background: var(--accent);
  border-color: var(--accent);
  box-shadow: 0 0 10px rgba(accent, 0.5);
}
```

## 11. Data Tables

```css
.data-table { width: 100%; border-collapse: collapse; font-size: 17px; }
.data-table th {
  background: var(--secondary);
  color: white;
  padding: 12px 18px;
  border-bottom: 3px solid var(--primary);
}
.data-table td { padding: 10px 18px; border-bottom: 1px solid #ddd; }
.data-table tr:nth-child(even) { background: var(--light-bg); }
.data-table tr:last-child { font-weight: 700; border-top: 2px solid var(--secondary); }
```

## 12. Print/PDF CSS

Handle the mismatch between slide size (1920x1080) and paper size:

```css
@page { size: 17in 11in; margin: 0; }
@media print {
  body { background: white; margin: 0; padding: 0; width: 17in; }
  section.slide {
    margin: 0;
    box-shadow: none;
    zoom: 0.85;  /* scales layout to fit Ledger paper */
    page-break-after: always;
    page-break-inside: avoid;
  }
}
```

Use `zoom` (not `transform: scale`) because zoom affects layout flow -- the slide fills the page with no gaps. The browser view is unaffected since `@media print` only applies during PDF export.

PDF generation command:
```bash
npx playwright pdf presentation.html presentation.pdf --paper-format=Ledger
```
