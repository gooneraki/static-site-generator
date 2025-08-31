import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_props_to_html_p(self):
        node = LeafNode(
            "a",
            "Take me there!",
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com" target="_blank" >Take me there!</a>',
        )

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello monsier")
        self.assertEqual(node.to_html(), "<h1>Hello monsier</h1>")
