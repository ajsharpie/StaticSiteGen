from enum import Enum

class HTMLTag(Enum):
    HEADING = "h"
    PARAGRAPH = "p"
    LINK = "a"
    ORDERED_LIST = "ol"
    UNORDER_LIST = "ul"
    LIST_ITEM = "li"
    QUOTE = "blockquote"
    CODE = "code"
    IMAGE = "img"

    


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def __eq__(self, other):
        if self.tag == other.tag:
            if self.value == other.value:
                if self.children == other.children:
                    if self.props == other.props:
                        return True
        return False
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        return "".join(map(lambda i: f" {i}={self.props[i]}", self.props))
                       
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        
    def to_html(self):
        if self.value == None:
            raise ValueError("Node requires a value")
        if self.tag == None:
            return self.value
        if self.tag == 'img':
            return f"<img{self.props_to_html()}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("no tag assigned")
        if self.children is None:
            raise ValueError("no children assigned")
        html_children = "".join(map(lambda x: x.to_html(), self.children))
        return f"<{self.tag}{self.props_to_html()}>{"".join(html_children)}</{self.tag}>"