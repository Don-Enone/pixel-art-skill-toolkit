import unittest

from pixel_art_skill_toolkit.renderer import render_document


class RendererTest(unittest.TestCase):
    def test_render_rect(self) -> None:
        document = {
            "version": "0.1",
            "canvas": {"width": 4, "height": 4, "background": None},
            "palette": {"red": "#ff0000"},
            "operations": [{"op": "rect", "color": "red", "x": 1, "y": 1, "w": 2, "h": 2}],
        }

        image = render_document(document)

        self.assertEqual(image.size, (4, 4))
        self.assertEqual(image.getpixel((1, 1)), (255, 0, 0, 255))
        self.assertEqual(image.getpixel((0, 0)), (0, 0, 0, 0))

    def test_render_stamp_component(self) -> None:
        document = {
            "version": "0.1",
            "canvas": {"width": 4, "height": 4, "background": None},
            "palette": {"blue": "#0000ff"},
            "components": {"dot": [{"op": "pixels", "color": "blue", "points": [[0, 0]]}]},
            "operations": [{"op": "stamp", "component": "dot", "x": 2, "y": 3}],
        }

        image = render_document(document)

        self.assertEqual(image.getpixel((2, 3)), (0, 0, 255, 255))


if __name__ == "__main__":
    unittest.main()
