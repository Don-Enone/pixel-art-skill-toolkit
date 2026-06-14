from __future__ import annotations

from copy import deepcopy
from typing import Any


def default_document() -> dict[str, Any]:
    """Return a small editable starter document."""
    return deepcopy(
        {
            "version": "0.1",
            "canvas": {"width": 16, "height": 16, "background": None},
            "palette": {
                "outline": "#1b1b1b",
                "body": "#69d46f",
                "highlight": "#d7ffd9",
            },
            "layers": [
                {
                    "name": "sprite",
                    "operations": [
                        {
                            "op": "ellipse",
                            "color": "body",
                            "x": 3,
                            "y": 5,
                            "w": 10,
                            "h": 8,
                        },
                        {
                            "op": "outline_rect",
                            "color": "outline",
                            "x": 4,
                            "y": 7,
                            "w": 8,
                            "h": 4,
                        },
                        {
                            "op": "pixels",
                            "color": "highlight",
                            "points": [[6, 6], [7, 6], [6, 7]],
                        },
                    ],
                }
            ],
        }
    )


def pretty_json(document: dict[str, Any]) -> str:
    import json

    return json.dumps(document, indent=2, ensure_ascii=False) + "\n"

