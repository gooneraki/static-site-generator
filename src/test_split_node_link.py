import unittest
from functions import split_nodes_link
from textnode import TextNode, TextType


class TestSplitNodeLink(unittest.TestCase):

    def test_split_links(self):
        node = TextNode(
            "This is text with a [Google](https://www.google.com/) and another [DuckDuckGo](https://duckduckgo.com/)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com/"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("DuckDuckGo", TextType.LINK, "https://duckduckgo.com/"),
            ],
            new_nodes,
        )

    def test_split_links_none(self):
        node = TextNode(
            "This is text without anything",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text without anything", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_both_start_and_end(self):
        node = TextNode(
            "This is text with a [Google](https://www.google.com/) and another [DuckDuckGo](https://duckduckgo.com/) and yei",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com/"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("DuckDuckGo", TextType.LINK, "https://duckduckgo.com/"),
                TextNode(" and yei", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_no_start_nor_end(self):
        node = TextNode(
            "[Google](https://www.google.com/) and another [DuckDuckGo](https://duckduckgo.com/)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Google", TextType.LINK, "https://www.google.com/"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("DuckDuckGo", TextType.LINK, "https://duckduckgo.com/"),
            ],
            new_nodes,
        )

    def test_split_links_no_text(self):
        node = TextNode(
            "[Google](https://www.google.com/)[DuckDuckGo](https://duckduckgo.com/)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Google", TextType.LINK, "https://www.google.com/"),
                TextNode("DuckDuckGo", TextType.LINK, "https://duckduckgo.com/"),
            ],
            new_nodes,
        )
