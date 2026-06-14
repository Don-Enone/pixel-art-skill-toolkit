# Pixel Art Skill Toolkit

**Language:** [English](../README.md) | [简体中文](readme.zh-CN.md) | 日本語 | [Español](readme.es.md) | [Français](readme.fr.md) | [Deutsch](readme.de.md)

Pixel Art Skill Toolkit は、AI 支援のピクセルアート制作向けのオープンソースツールキットです。コンパクトで人間が編集しやすい Pixel Art JSON 形式を定義し、その JSON を PNG にレンダリングします。AI が生成したソースを確認、編集するための軽量なデスクトップ GUI も含まれています。

基本方針：AI は完全なピクセル行列、Base64 画像、長い ASCII スプライトを出力しません。代わりに、パレット、レイヤー、描画操作、再利用可能な stamp などの高レベルな描画指示を出力します。

## Features

- Reusable AI skill: `skill/pixel-art-json/SKILL.md`
- Compact Pixel Art JSON format
- JSON-to-PNG renderer with transparent background support
- Integer nearest-neighbor scaling
- Tkinter GUI for JSON, palette, operations, preview, save, and PNG export
- Examples, documentation, and JSON Schema

## Install

```bash
git clone https://github.com/Don-Enone/pixel-art-skill-toolkit.git
cd pixel-art-skill-toolkit
python -m pip install -e .
```

Python 3.10+ と Pillow が必要です。Tkinter は多くのデスクトップ Python 環境に含まれています。

## Render

```bash
pixel-art-render examples/slime.json -o slime.png --scale 12
```

## GUI

```bash
pixel-art-gui
```

またはファイルを直接開きます。

```bash
pixel-art-toolkit gui examples/slime.json
```

## Documentation

- [JSON format](json-format.md)
- [GUI editor](gui.md)
- [Skill usage](skill-usage.md)
- [JSON Schema](../schema/pixel-art.schema.json)

## License

MIT

