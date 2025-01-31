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
        
    def to_html(self):
        if self.value == None:
            raise ValueError("Node requires a value")
        if self.tag == None:
            return self.value    
        match self.tag:
            case None:
                return self.value
            case HTMLTag.HEADING.value:
                tag = f"h{self.props["level"]}"
                return f"<{tag}>{self.value}</{tag}>"
            
            case HTMLTag.PARAGRAPH.value:
                return self.add_tags(self.value)
            
            case HTMLTag.LINK.value:
                return f"<a{self.props_to_html()}>{self.value}</a>"
            
            case HTMLTag.LIST_ITEM.value:
                return f"<il>{self.value}</il>"
            
 #           case HTMLTag.ORDERED_LIST.value:  #I dont think lists of either kind CAN be leaves - since they imply child
 #               items = "\t"+"\n\t".join(self.props.values())
 #               return f"<ol>\n{items}\n</ol>"
            
  #          case HTMLTag.UNORDER_LIST.value:
                
  #              items = "\t"+"\n\t".join(self.props.values())
  #              return f"<ul>\n{items}\n</ul>"
            
            case HTMLTag.CODE.value:
                return self.add_tags(self.props_to_html())
            
            case HTMLTag.IMAGE.value:
                return f"<img{self.props_to_html()} />"
            
            case _:
                raise ValueError("No valid tag found")           
        return Exception("unknown error")
        
    def add_tags(self, rep):
        return f"<{self.tag}>{rep}</{self.tag}>"