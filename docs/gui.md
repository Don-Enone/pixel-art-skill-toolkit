# GUI Editor

The GUI editor is intentionally small. Its purpose is to make AI-generated Pixel Art JSON easier to inspect and edit, not to replace a professional pixel art application.

## Open

```bash
pixel-art-gui
```

Or:

```bash
python -m pixel_art_skill_toolkit gui examples/slime.json
```

## Features

- Open Pixel Art JSON files
- Preview rendered output
- Edit raw JSON
- Format JSON
- Edit palette entries
- Add, edit, or delete drawing operations
- Save JSON
- Export PNG at an integer scale

## Workflow

1. Open a JSON file.
2. Use the preview to inspect the rendered sprite.
3. Change raw JSON directly or use the Palette and Operations tabs.
4. Click `Apply JSON` or `Render`.
5. Save the JSON or export a PNG.

