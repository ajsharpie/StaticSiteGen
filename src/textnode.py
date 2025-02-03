from enum import Enum
from htmlnode import *



class TextType(Enum):
    TEXT = None
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"
    
class TextNode:
    def __init__(self, text, type, url=None, alt=None):
        self.text = text
        self.type = type
        self.url = url
        self.alt = alt
        
        
        
    def __eq__(self, TextNode):
        if self.text == TextNode.text:
            if self.type == TextNode.type:
                if self.url == TextNode.url:
                    return True     
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.type}, {self.url}, {self.alt})"
    
    def text_to_html(self):
        if self.type.value == 'a':
            return LeafNode(self.type.value, self.text, {'href': self.url})            
        if self.type.value == 'img':
            return LeafNode(self.type.value, '', {'src': self.url, 'alt': self.alt})
        return LeafNode(self.type.value, self.text)
                
    