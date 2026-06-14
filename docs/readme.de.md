# Pixel Art Skill Toolkit

**Sprache:** [English](../README.md) | [简体中文](readme.zh-CN.md) | [日本語](readme.ja.md) | [Español](readme.es.md) | [Français](readme.fr.md) | Deutsch

Pixel Art Skill Toolkit ist ein Open-Source-Toolkit für KI-gestützte Pixelkunst. Es definiert ein kompaktes, menschenlesbares Pixel Art JSON Format, rendert dieses JSON zu PNG und enthält einen schlanken Desktop-Editor zum Prüfen und Bearbeiten KI-generierter Quelldateien.

Grundidee: Die KI soll keine vollständige Pixelmatrix, kein Base64-Bild und keinen langen ASCII-Sprite ausgeben. Stattdessen erzeugt sie höherwertige Zeichenanweisungen wie Paletten, Ebenen, Operationen und wiederverwendbare Stamps.

## Funktionen

- Wiederverwendbarer KI-Skill: `skill/pixel-art-json/SKILL.md`
- Kompaktes Pixel Art JSON Format
- JSON-zu-PNG-Renderer mit transparentem Hintergrund
- Ganzzahlige nearest-neighbor Skalierung
- Tkinter-GUI für JSON, Palette, Operationen, Vorschau, Speichern und PNG-Export
- Beispiele, Dokumentation und JSON Schema

## Installation

```bash
git clone https://github.com/Don-Enone/pixel-art-skill-toolkit.git
cd pixel-art-skill-toolkit
python -m pip install -e .
```

Benötigt Python 3.10+ und Pillow.

## Rendern

```bash
pixel-art-render examples/slime.json -o slime.png --scale 12
```

## GUI

```bash
pixel-art-gui
```

Oder eine Datei direkt öffnen:

```bash
pixel-art-toolkit gui examples/slime.json
```

## Dokumentation

- [JSON Format](json-format.md)
- [GUI Editor](gui.md)
- [Skill Nutzung](skill-usage.md)
- [JSON Schema](../schema/pixel-art.schema.json)

## Lizenz

MIT

