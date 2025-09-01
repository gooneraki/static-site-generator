from htmlnode import LeafNode

from textnode import TextNode, TextType
import re

images_patern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
links_patern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)

        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)

        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)

        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)

        case TextType.LINK:
            return LeafNode(
                tag="a", value=text_node.text, props={"href": text_node.url}
            )

        case TextType.IMAGE:
            return LeafNode(
                tag="img",
                value=None,
                props={"src": text_node.url, "alt": text_node.text},
            )

        case default:
            raise ValueError("Invalid text_type for TextNode")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):

    return re.findall(images_patern, text)


def extract_markdown_links(text):

    return re.findall(links_patern, text)


def split_nodes_image(old_nodes):
    return split_nodes_any(old_nodes, extract_markdown_images, TextType.IMAGE)


def split_nodes_link(old_nodes):
    return split_nodes_any(old_nodes, extract_markdown_links, TextType.LINK)


def split_nodes_any(old_nodes, markdown_fn, new_text_type):
    new_nodes = []
    for old_node in old_nodes:
        split_nodes = []

        image_tuples = markdown_fn(old_node.text)

        if len(image_tuples) == 0:
            new_nodes.append(old_node)
            continue

        text_to_break = old_node.text

        for idx in range(len(image_tuples)):

            image_tuple = image_tuples[idx]

            delim = (
                "!" if new_text_type == TextType.IMAGE else ""
            ) + f"[{image_tuple[0]}]({image_tuple[1]})"

            sections = text_to_break.split(delim)

            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], old_node.text_type))

            split_nodes.append(TextNode(image_tuple[0], new_text_type, image_tuple[1]))
            text_to_break = sections[1]

            if idx == len(image_tuples) - 1 and sections[1] != "":
                split_nodes.append(TextNode(sections[1], old_node.text_type))

        new_nodes.extend(split_nodes)

    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    return nodes
