# Pixel Art Skill Toolkit

**Idioma:** [English](../README.md) | [简体中文](readme.zh-CN.md) | [日本語](readme.ja.md) | Español | [Français](readme.fr.md) | [Deutsch](readme.de.md)

Pixel Art Skill Toolkit es un conjunto de herramientas de código abierto para pixel art asistido por IA. Define un formato Pixel Art JSON compacto y editable por humanos, renderiza ese JSON a PNG e incluye un editor de escritorio ligero para revisar y modificar archivos generados por IA.

Idea principal: la IA no debe generar una matriz completa de píxeles, una imagen Base64 ni un sprite ASCII largo. En su lugar, genera instrucciones de dibujo de alto nivel: paletas, capas, operaciones y stamps reutilizables.

## Funciones

- Skill reutilizable para IA: `skill/pixel-art-json/SKILL.md`
- Formato Pixel Art JSON compacto
- Renderizador de JSON a PNG con fondo transparente
- Escalado entero con nearest-neighbor
- GUI con Tkinter para JSON, paleta, operaciones, vista previa, guardado y exportación PNG
- Ejemplos, documentación y JSON Schema

## Instalación

```bash
git clone https://github.com/Don-Enone/pixel-art-skill-toolkit.git
cd pixel-art-skill-toolkit
python -m pip install -e .
```

Requiere Python 3.10+ y Pillow.

## Renderizar

```bash
pixel-art-render examples/slime.json -o slime.png --scale 12
```

## GUI

```bash
pixel-art-gui
```

O abre un archivo directamente:

```bash
pixel-art-toolkit gui examples/slime.json
```

## Documentación

- [Formato JSON](json-format.md)
- [Editor GUI](gui.md)
- [Uso del Skill](skill-usage.md)
- [JSON Schema](../schema/pixel-art.schema.json)

## Licencia

MIT

