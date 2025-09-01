import unittest
from markdown_blocks import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):

    def test_heading_1(self):
        block = "# This is a heading 1"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.HEADING)

        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading_6(self):
        block = "###### This is a heading 6"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_bad_6(self):
        block = "######This is a bad heading 6"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_heading_7(self):
        block = "####### This is not a heading as it has 7"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_code_1(self):
        block = "```\nThis is a code block\n```"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.CODE)

    def test_code_2(self):
        block = "```\n```"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.CODE)

    def test_code_4(self):
        block = "`` Code block 2 thingys ``"
        block_type = block_to_block_type(block)

        self.assertNotEqual(block_type, BlockType.CODE)
