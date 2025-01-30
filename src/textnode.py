from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
class TextNode:
    def __init__(self, text, type, url=None):
        self.text = text
        self.type = type
        self.url = url
        
        
        
    def __eq__(self, TextNode):
        if self.text == TextNode.text:
            if self.type == TextNode.type:
                if self.url == TextNode.url:
                    return True     
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"
    

    