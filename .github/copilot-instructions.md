# GitHub Copilot Instructions for Documentation Project

This file provides guidance for GitHub Copilot when writing, editing, and improving technical documentation in this MkDocs project.

## Language and Style

- Use **concise, clear, and factual language**
- Avoid unnecessary filler words, marketing tone, or repetition
- Prefer **active voice** over passive voice
- Keep sentences **short and direct** (aim for 15-20 words per sentence)
- Write in a **professional, direct, and reader-focused** tone

## Markdown Formatting

Follow correct Markdown syntax at all times. Prefer MkDocs-compatible styling and the repository's existing conventions.

- Use proper heading hierarchy (`#`, `##`, `###`, etc.)
- Format code blocks with appropriate language tags (for example: ```python or ```bash)
- Create valid links: `[link text](URL)` or `[link text](relative/path.md)`
- Use consistent list formatting (either `-` or `*` for unordered lists, `1.` for ordered)
- Format inline code with single backticks: `` `code` ``
- Use tables correctly with proper alignment

Important formatting notes:

!!! note "Blank line before lists"

	When creating a list, include a blank line before the list block. This ensures correct rendering across MkDocs themes and avoids incorrect nesting in some renderers.

!!! note "Admonitions"

	Use MkDocs-style admonitions for inline guidance instead of plain bold/italic labels. Examples:

	- `!!! note "Note"` for informational notes
	- `!!! tip "Tip"` for helpful hints
	- `!!! warning "Warning"` for cautions
	- `!!! important "Important"` for critical points

	Admonitions should be used for notes, warnings, important caveats, or any UI/behavioral exceptions that readers must see.

## Terminology and Consistency

- Maintain **consistent terminology** throughout all documentation
- Use standard **units and measurements** consistently
- Follow the existing **style conventions** in the project
- Preserve capitalization patterns (e.g., product names, technical terms)
- Keep acronyms consistent (define on first use, then use abbreviated form)

## Code Examples

All code examples should be:

- **Correct and tested** (or clearly marked as pseudocode)
- **Minimal** - include only what's necessary to demonstrate the concept
- **Well-commented** when complexity requires explanation
- **Properly formatted** with appropriate syntax highlighting
- **Relevant** to the surrounding documentation context

## Document Structure

When editing existing documents:

- **Preserve the existing structure** (headings, sections, flow)
- Maintain the established organization and hierarchy
- Don't reorganize content unless explicitly requested
- Keep related information grouped together
- Respect existing navigation patterns and cross-references

## Handling Uncertainty

If uncertain about a technical fact or detail:

- **Flag it** with a comment like `<!-- TODO: Verify this detail -->`
- Use qualifying language ("typically", "generally", "may")
- Suggest verification rather than stating as absolute fact
- Do not fabricate technical specifications or requirements

## Documentation Conventions

- **Respect all existing conventions** in this project
- Do not introduce stylistic drift or inconsistencies
- Follow the patterns established in existing documentation
- Match the tone and formality level of surrounding content
- Preserve any project-specific formatting or notation systems

---

**Remember:** Your role is to enhance clarity and accuracy while maintaining consistency with the existing documentation standards. When in doubt, preserve what's already there rather than introducing changes.