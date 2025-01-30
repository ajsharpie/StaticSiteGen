import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_repr_eq(self):
        node = TextNode("this IS a TextNode", TextType.ITALIC, "url stuff goes here")
        node2 = TextNode("this IS a TextNode", TextType.ITALIC, "url stuff goes here")
        self.assertEqual(node.__repr__(), node2.__repr__())
        
    def test_noteq(self):
        node = TextNode("this IS a TextNode", TextType.ITALIC, "url stuff goes here")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_not_repr_eq(self):
        node = TextNode("this IS a TextNode", TextType.ITALIC, "url stuff goes here")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node.__repr__(), node2.__repr__())
    
    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "urlstuffhere")
        node2 = TextNode("This IS a text node", TextType.BOLD)
        self.assertNotEqual(node.text, node2.text)
        
    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, node2.url)
        
        
if __name__ == "__main__":
    unittest.main()