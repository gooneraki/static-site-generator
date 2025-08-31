import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            tag="a", props={"href": "https://www.google.com", "target": "_blank"}
        )
        node2 = HTMLNode(
            tag="a", props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(node.__repr__(), node2.__repr__())

    def test_not_eq(self):
        node = HTMLNode(
            tag="a", props={"href": "https://www.google.com", "target": "_blank"}
        )
        node2 = HTMLNode(tag="a", props={"href": "https://www.google.com"})
        self.assertNotEqual(node.__repr__(), node2.__repr__())

    def test_tags(self):
        node = HTMLNode(tag="a")
        node2 = HTMLNode(tag="h1")
        self.assertNotEqual(node.__repr__(), node2.__repr__())
