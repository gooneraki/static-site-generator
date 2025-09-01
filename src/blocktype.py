from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(md_text):
    print(f"block_to_block_type(\n{md_text}\n)")
    heading_pattern = r"^#{1,6} "
    if re.match(heading_pattern, md_text):
        return BlockType.HEADING

    code_pattern = r"^\`{3}.*\`{3}$"
    if re.match(code_pattern, md_text):
        return BlockType.CODE

    if md_text.startswith(">"):
        return BlockType.QUOTE

    if md_text.startswith("- "):
        return BlockType.UNORDERED_LIST

    if md_text.startswith("1. "):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
