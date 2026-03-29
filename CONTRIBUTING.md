# Contributing

Contributions are welcome. Here's how to help.

## What to Contribute

- **Slide layout patterns** -- Add new CSS Grid patterns to `references/layout_patterns.md` (e.g., three-column layouts, image galleries, comparison slides)
- **Chart templates** -- Add matplotlib script templates to `scripts/` for common chart types
- **Skill improvements** -- Bug fixes, clearer instructions, or better prompting patterns in `SKILL.md`
- **Examples** -- Add example storyboards, style guides, or screenshots of presentations you've built

## How to Contribute

1. Fork the repo
2. Create a branch (`git checkout -b my-improvement`)
3. Make your changes
4. Test by copying the skill to `~/.claude/skills/presentation-builder/` and running it
5. Submit a pull request with a clear description of what changed and why

## Guidelines

- Keep `SKILL.md` under 500 lines (it loads into Claude's context every time)
- Reference files in `references/` can be longer -- they're loaded on demand
- Test your changes by actually building a presentation with the skill
- Don't commit generated files (PNGs, PDFs, HTML presentations) -- only source files and examples
