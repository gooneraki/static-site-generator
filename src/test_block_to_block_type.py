import unittest
from blocktype import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):

    def test_heading_1(self):
        block = "# This is a heading 1"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.HEADING)

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
        block = "``` This is a code block ```"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.CODE)

    def test_code_2(self):
        block = "``````"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.CODE)

    def test_code_3(self):
        block = "```` Code block 4 on the left ```"
        block_type = block_to_block_type(block)

        self.assertEqual(block_type, BlockType.CODE)

    def test_code_4(self):
        block = "`` Code block 2 thingys ``"
        block_type = block_to_block_type(block)

        self.assertNotEqual(block_type, BlockType.CODE)


#     def test_markdown_to_blocks(self):
#         md = """
# This is **bolded** paragraph

# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line

# - This is a list
# - with items
# """
#         blocks = markdown_to_blocks(md)

#         self.assertEqual(
#             blocks,
#             [
#                 "This is **bolded** paragraph",
#                 "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
#                 "- This is a list\n- with items",
#             ],
#         )

#     def test_markdown_to_blocks_v2(self):
#         md = """
# # This is a heading

# This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

# - This is the first list item in a list block
# - This is a list item
# - This is another list item
# """
#         blocks = markdown_to_blocks(md)

#         self.assertEqual(
#             blocks,
#             [
#                 "# This is a heading",
#                 "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
#                 "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
#             ],
#         )
