import unittest
from random import randint

from htmlnode import HTMLNode, HTMLTag, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("code", "value", "children", "props")
        node2 = HTMLNode("code", "value", "children", "props")
        self.assertEqual(node, node2)
        
    def test_repr_eq(self):
        node = HTMLNode("ul", "value", "child", "props")
        node2 = HTMLNode("ul", "value", "child", "props")
        self.assertEqual(node.__repr__(), node2.__repr__())
        
    def test_not_eq(self):
        node = HTMLNode('l', "value", "child", "props123")
        node2 = HTMLNode('c', "value123", "child", "props")
        self.assertNotEqual(node, node2)
        
    def test_props_eq(self):
        node = HTMLNode(None, "value", "child", "1234")
        node2 = HTMLNode('p', "value", "child", "1234")
        self.assertEqual(node.props, node2.props)
        
    
        
class TestLeafNode(unittest.TestCase):
        
    def test_paragraph(self):
        node = LeafNode("p", "This is a paragraph\nIt has multiple lines and stuff!\n Wow!", None).to_html()
        self.assertTrue(node.startswith("<p>") and node.endswith("</p>") and "stuff" in node)
        
    def test_link(self):
        node = LeafNode("a", "click me!", {"href": "boot.dev", "target": "_sometarget"})
        self.assertEqual(node.to_html(), "<a href=boot.dev target=_sometarget>click me!</a>")