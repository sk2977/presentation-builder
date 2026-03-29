# Presentation Builder

A Claude Code skill that creates professional, branded slide presentations from storyboards or from scratch. Produces HTML/CSS decks with data charts, AI-generated illustrations, and structured layouts -- exported as PDF.

## What It Does

Tell Claude to build a presentation and this skill handles the entire pipeline:

1. **Research** the topic (optional -- deploys parallel agents)
2. **Create a storyboard** in markdown with slide-by-slide content
3. **Generate a style guide** from brand colors (or use an existing one)
4. **Build data charts** with matplotlib (pie, bar, line, dual-axis, stacked)
5. **Generate illustrations** with Recraft V3 (optional -- characters, objects, icons)
6. **Assemble the deck** as a single HTML file with CSS Grid layouts
7. **Verify** each slide visually with Playwright screenshots
8. **Export to PDF** for presenting

The result looks like it was designed by a professional agency -- not a PowerPoint template.

## Installation

### Option 1: Copy to your skills directory

```bash
# Clone the repo
git clone https://github.com/skimb/presentation-builder.git

# Copy to Claude Code skills directory
cp -r presentation-builder ~/.claude/skills/presentation-builder
```

### Option 2: Symlink (for development)

```bash
git clone https://github.com/skimb/presentation-builder.git
ln -s "$(pwd)/presentation-builder" ~/.claude/skills/presentation-builder
```

After installation, Claude Code will automatically detect the skill when you mention presentations, slides, or decks.

## Requirements

**Required:**
- Claude Code (CLI, desktop app, or IDE extension)
- Python 3.x with matplotlib and Pillow

**Optional (but recommended):**
- Playwright (`npx playwright install chromium`) -- for visual verification and PDF export
- Recraft V3 API key -- for AI-generated illustrations ($0.04-0.08/image)

## Setup (Optional: Recraft Illustrations)

If you want AI-generated illustrations (characters, objects, icons):

1. Get an API key at [recraft.ai](https://www.recraft.ai) (Profile > API)
2. Create a `.env` file in your project directory:

```bash
cp .env.example .env
# Edit .env and add your API key
```

Without Recraft, the skill uses Claude-generated inline SVG (free, decent quality) or icon libraries.

## Usage

Just tell Claude what you need:

```
"Create a 5-slide presentation about renewable energy trends for an investor audience. Use dark green and navy."
```

```
"I have a storyboard in storyboard.md and a style guide. Build the slides and export to PDF."
```

```
"I'm giving a 30-minute workshop to MBA students about venture capital in climate tech. Research the topic and build the full deck."
```

The skill will:
- Ask clarifying questions if needed (audience, duration, brand colors)
- Skip steps you've already done (if storyboard exists, it won't recreate it)
- Use Recraft if an API key is available, otherwise fall back to inline SVG
- Generate a PDF for presenting and an HTML file for browser viewing

## Output

```
your-project/
  storyboard.md            # Slide content and narrative
  style_guide.md           # Brand colors, typography, component specs
  presentation.html        # The deck (open in browser to present)
  presentation.pdf         # PDF export (for sharing/projecting)
  graphics/
    src/
      chart_style.py       # Shared matplotlib config
      *.py                 # One script per chart
      generate_recraft.py  # Recraft API script (if used)
    *.png                  # Chart images
    recraft_*.png          # AI illustrations (if Recraft used)
```

## Visual Tiers

The skill adapts to available tools:

| Tier | Illustrations | Charts | Cost |
|------|--------------|--------|------|
| **Clean** | None (text + charts only) | matplotlib | Free |
| **SVG** | Claude-generated inline SVG | matplotlib | Free |
| **Illustrated** | Recraft V3 AI illustrations | matplotlib | ~$0.50 |

## How It Works

Each slide uses CSS Grid for precise layout:

```
+--------------------------------------------------+
| Header (title + subtitle)              | full width |
+-------------------------------------+------------+
| Content                              | Sidebar    |
| (stats, text, charts)               | (callout   |
|                                      |  box)      |
+-------------------------------------+------------+
| Audience Question / Key Takeaway       | full width |
+--------------------------------------------------+
| Timeline (progressive dots)            | full width |
+--------------------------------------------------+
```

- **1920x1080px** slides (16:9 standard)
- **CSS Grid** layout with content + sidebar columns
- **Charts expand** to fill available space (no fixed max-height)
- **Print CSS** scales slides to fit Ledger paper for PDF export

## Slide Components

- **Stat boxes** -- key numbers with branded bottom border
- **Data tables** -- dark header, alternating rows
- **Callout/sidebar boxes** -- dark background with accent border
- **Audience questions** -- full-width bar with brand-color left border
- **Quote blocks** -- italic, muted, left border accent
- **Progress timeline** -- circles connected by lines, progressively highlighted
- **2x2 matrices** -- colored quadrants with axis labels
- **Inline SVG icons** -- or Recraft illustrations if available

## Examples

See the `examples/` directory for sample presentations built with this skill.

## Contributing

Contributions welcome. Key areas:
- Additional slide layout patterns (in `references/layout_patterns.md`)
- Chart type templates (in `scripts/`)
- Bug fixes and improvements to `SKILL.md`

## License

MIT
