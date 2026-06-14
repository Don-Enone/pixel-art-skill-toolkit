---
name: pixel-art-json
description: Generate and edit pixel art as compact, high-level JSON drawing instructions for the Pixel Art Skill Toolkit renderer instead of full pixel matrices, Base64 images, long ASCII grids, or verbose coordinate dumps. Use when creating, modifying, or explaining pixel-art sprites, icons, tiles, game assets, UI assets, or tiny illustrations where token-efficient, human-editable source is preferred.
---

# Pixel Art JSON

Generate Pixel Art JSON that a renderer can turn into PNG. Keep the source compact, readable, and easy for a human to edit.

## Core Rules

- Output JSON, not a PNG, Base64 string, ASCII grid, SVG, or full per-pixel matrix.
- Use a small canvas such as `16x16`, `24x24`, `32x32`, `48x48`, or `64x64`.
- Use a named `palette`; reference palette keys from drawing operations.
- Prefer high-level operations: `rect`, `outline_rect`, `ellipse`, `line`, `path`, `polygon`, `stamp`.
- Use `pixels` only for small details, highlights, face pixels, texture, and cleanup.
- Reuse repeated shapes with `components` and `stamp`.
- Keep edits localized: preserve existing JSON and change only relevant palette entries, components, layers, or operations.

## Output Shape

Use this structure:

```json
{
  "version": "0.1",
  "canvas": { "width": 24, "height": 24, "background": null },
  "palette": {
    "outline": "#1b1b1b",
    "body": "#55c96f",
    "highlight": "#a7f59c"
  },
  "components": {},
  "layers": [
    {
      "name": "sprite",
      "operations": [
        { "op": "ellipse", "color": "body", "x": 4, "y": 5, "w": 15, "h": 12 },
        { "op": "pixels", "color": "highlight", "points": [[8, 7], [9, 7]] }
      ]
    }
  ]
}
```

## Operations

Use integer coordinates. The origin is the top-left pixel.

- `rect`: `{ "op": "rect", "color": "body", "x": 4, "y": 6, "w": 12, "h": 8 }`
- `outline_rect`: `{ "op": "outline_rect", "color": "outline", "x": 4, "y": 6, "w": 12, "h": 8 }`
- `ellipse`: `{ "op": "ellipse", "color": "body", "x": 4, "y": 5, "w": 14, "h": 10 }`
- `line`: `{ "op": "line", "color": "outline", "x1": 2, "y1": 2, "x2": 10, "y2": 7 }`
- `path`: `{ "op": "path", "color": "outline", "points": [[2, 2], [4, 4], [7, 4]] }`
- `polygon`: `{ "op": "polygon", "color": "body", "points": [[8, 2], [14, 8], [3, 8]] }`
- `pixels`: `{ "op": "pixels", "color": "shine", "points": [[6, 6], [7, 6], [6, 7]] }`
- `erase`: `{ "op": "erase", "points": [[2, 2], [3, 2]] }`
- `stamp`: `{ "op": "stamp", "component": "eye", "x": 10, "y": 13 }`

## Component Pattern

Use components for repeated motifs:

```json
{
  "components": {
    "eye": [
      { "op": "rect", "color": "outline", "x": 0, "y": 0, "w": 4, "h": 3 },
      { "op": "rect", "color": "white", "x": 1, "y": 1, "w": 2, "h": 1 }
    ]
  },
  "layers": [
    {
      "name": "face",
      "operations": [
        { "op": "stamp", "component": "eye", "x": 6, "y": 8 },
        { "op": "stamp", "component": "eye", "x": 14, "y": 8 }
      ]
    }
  ]
}
```

## Editing Existing JSON

When asked to modify existing pixel art:

1. Identify the smallest relevant change.
2. Prefer changing palette values for color edits.
3. Add or adjust a layer for accessories, effects, or new details.
4. Add a component when a motif repeats.
5. Avoid rewriting unchanged layers.
6. Avoid expanding `pixels` into large coordinate lists.

For patch-style replies, show only the changed JSON object or a concise before/after snippet unless the user requests the full file.

