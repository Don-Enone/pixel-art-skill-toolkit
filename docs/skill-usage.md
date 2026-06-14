# Pixel Art Skill Usage

The portable skill is in:

```text
skill/pixel-art-json/SKILL.md
```

Copy that folder into a Codex skills directory, or adapt the contents for another AI assistant that supports reusable instructions.

## Intended Use

Use the skill when an AI needs to create or modify pixel art but should avoid expensive output formats such as:

- Full per-pixel matrices
- Base64 image strings
- Long ASCII art grids
- Repeated coordinate dumps for every pixel

The expected AI output is a concise Pixel Art JSON document. A renderer then turns the JSON into a PNG.

## Typical Prompt

```text
Use the Pixel Art JSON format to create a 24x24 transparent-background potion icon.
Keep the output compact and use palette keys, reusable components, and high-level operations.
```

## Editing Existing Art

When editing an existing file, ask the AI to return a patch or a replacement JSON document that only changes the necessary operations.

Example:

```text
Modify this Pixel Art JSON so the slime has a small crown. Preserve the palette and existing body operations unless needed.
```

The skill instructs the AI to add a small component or layer instead of rewriting the whole document.

