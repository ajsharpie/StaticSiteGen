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
        
        match type:
            case "normal": 
                self.type = TextType.NORMAL
            case "bold": 
                self.type = TextType.BOLD
            case "italic": 
                self.type = TextType.ITALIC
            case "code": 
                self.type = TextType.CODE
            case "link": 
                self.type = TextType.LINK
            case "image": 
                self.type = TextType.IMAGE
            case _:
                self.type = None
        
        
    def __eq__(self, TextNode):
        if self.text == TextNode.text:
            if self.type == TextNode.type:
                if self.url == TextNode.url:
                    return True     
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"
    

    