import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ineq(self):
        node = TextNode("This is a node", TextType.BOLD)
        node2 = TextNode("This is a node", TextType.ITALIC)
        self.assertNotEqual(node, node2)


    def test_url_one_none(self):
        node = TextNode("This is a text node", TextType.BOLD, 'http:www.notnone.com')
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_not_none(self):
        node = TextNode("This is a text node", TextType.BOLD, 'http://www.notnone.com')
        node2 = TextNode("This is a text node", TextType.BOLD, 'http://www.notnone.com')
        self.assertEqual(node, node2)




if __name__ == "__main__":
    unittest.main()
