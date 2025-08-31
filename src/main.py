from textnode import TextNode, TextType
from htmlnode import LeafNode


def main():
    node = TextNode("This is some bold text", "bold", "http://www.bold.com")
    print(node)


main()
