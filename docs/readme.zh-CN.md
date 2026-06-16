# Pixel Art Skill Toolkit

**语言：** [English](../README.md) | 简体中文 | [日本語](readme.ja.md) | [Español](readme.es.md) | [Français](readme.fr.md) | [Deutsch](readme.de.md)

Pixel Art Skill Toolkit 是一个面向 AI 像素图生成的开源工具包。它提供一种简洁、可读、便于人工修改的 Pixel Art JSON 格式，并能将 JSON 渲染为 PNG，同时提供轻量级桌面 GUI 用于查看和编辑 AI 生成的像素图源文件。

核心思想：AI 不直接输出完整逐像素矩阵、Base64 图片或很长的 ASCII 图，而是输出调色板、图层、绘制操作和可复用 stamp 等高层级绘制描述。工具再根据这些描述生成真正的像素图 PNG。

## 功能

- 可复用 AI Skill：`skill/pixel-art-json/SKILL.md`
- 紧凑的 Pixel Art JSON 格式
- JSON 到 PNG 渲染器，支持透明背景
- 整数倍 nearest-neighbor 放大，保持像素画风格
- Tkinter GUI：编辑 JSON、调色板、绘制操作、预览、保存、导出 PNG
- 示例文件、格式文档和 JSON Schema

## 安装

```bash
git clone https://github.com/Don-Enone/pixel-art-skill-toolkit.git
cd pixel-art-skill-toolkit
python -m pip install -e .
```

需要 Python 3.10+ 和 Pillow。大多数桌面 Python 环境默认包含 Tkinter。

## 渲染图片

```bash
pixel-art-render examples/slime.json -o slime.png --scale 12
```

源码目录下未安装时：

```bash
PYTHONPATH=src python -m pixel_art_skill_toolkit render examples/slime.json -o slime.png --scale 12
```

PowerShell：

```powershell
$env:PYTHONPATH = "src"
python -m pixel_art_skill_toolkit render examples\slime.json -o slime.png --scale 12
```

## 打开 GUI

Windows 下可双击启动：

```text
launch_gui.bat
```

或使用 PowerShell：

```powershell
.\launch_gui.ps1
```

安装后也可以运行：

```bash
pixel-art-gui
```

或直接打开文件：

```bash
pixel-art-toolkit gui examples/slime.json
```

GUI 可以打开 Pixel Art JSON 文件、查看渲染预览、编辑原始 JSON、修改调色板、添加/编辑/删除绘制操作、保存 JSON、导出 PNG。

预览区域带滚动条，大比例像素图不会因为窗口边界而无法查看完整内容。

## 格式概览

```json
{
  "version": "0.1",
  "canvas": { "width": 16, "height": 16, "background": null },
  "palette": {
    "outline": "#1b1b1b",
    "body": "#69d46f",
    "shine": "#d7ffd9"
  },
  "layers": [
    {
      "name": "sprite",
      "operations": [
        { "op": "ellipse", "color": "body", "x": 3, "y": 5, "w": 10, "h": 8 },
        { "op": "outline_rect", "color": "outline", "x": 4, "y": 7, "w": 8, "h": 4 },
        { "op": "pixels", "color": "shine", "points": [[6, 6], [7, 6]] }
      ]
    }
  ]
}
```

完整格式说明见 [json-format.md](json-format.md)。

## 文档

- [JSON 格式](json-format.md)
- [GUI 编辑器](gui.md)
- [Skill 使用方式](skill-usage.md)
- [JSON Schema](../schema/pixel-art.schema.json)

## 许可证

MIT
