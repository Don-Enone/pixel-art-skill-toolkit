# Pixel Art Skill Toolkit

**Langue :** [English](../README.md) | [简体中文](readme.zh-CN.md) | [日本語](readme.ja.md) | [Español](readme.es.md) | Français | [Deutsch](readme.de.md)

Pixel Art Skill Toolkit est une boîte à outils open source pour le pixel art assisté par IA. Elle définit un format Pixel Art JSON compact et modifiable à la main, rend ce JSON en PNG et fournit un éditeur de bureau léger pour examiner et modifier les fichiers générés par l'IA.

Idée principale : l'IA ne doit pas produire une matrice complète de pixels, une image Base64 ou un long sprite ASCII. Elle produit plutôt des instructions de dessin de haut niveau : palettes, calques, opérations et stamps réutilisables.

## Fonctionnalités

- Skill IA réutilisable : `skill/pixel-art-json/SKILL.md`
- Format Pixel Art JSON compact
- Rendu JSON vers PNG avec fond transparent
- Mise à l'échelle entière en nearest-neighbor
- GUI Tkinter pour JSON, palette, opérations, aperçu, sauvegarde et export PNG
- Exemples, documentation et JSON Schema

## Installation

```bash
git clone https://github.com/Don-Enone/pixel-art-skill-toolkit.git
cd pixel-art-skill-toolkit
python -m pip install -e .
```

Nécessite Python 3.10+ et Pillow.

## Rendu

```bash
pixel-art-render examples/slime.json -o slime.png --scale 12
```

## GUI

```bash
pixel-art-gui
```

Ou ouvrez directement un fichier :

```bash
pixel-art-toolkit gui examples/slime.json
```

## Documentation

- [Format JSON](json-format.md)
- [Éditeur GUI](gui.md)
- [Utilisation du Skill](skill-usage.md)
- [JSON Schema](../schema/pixel-art.schema.json)

## Licence

MIT

