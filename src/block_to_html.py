from text_to_node import *
from htmlnode import *

def markdown_to_html_node(mdtext):
    blocks = markdown_to_blocks(mdtext)
    children = []
    for block in blocks:
        html_node =  block_to_html_node(block)
        children.append(html_node)
    return ParentNode('div', children)
        
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == 'p':
        return paragraph_to_html(block)
    if block_type == 'blockquote':
        return blockquote_to_html(block)
    if block_type == 'h':
        return heading_to_html(block)
    if block_type == 'code':
        return code_to_html(block)
    if block_type == 'lio':
        return org_list_to_html(block)
    if block_type == 'liu':
        return unorg_list_to_html(block)
    raise ValueError('bad block type')  

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(node.text_to_html()) 
    return children

def org_list_to_html(block):
    list_items = block.split('\n')
    html_items = []
    for item in list_items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode('li', children))
    return ParentNode('ol', html_items)

def unorg_list_to_html(block):
    list_items = block.split('\n')
    html_items = []
    for item in list_items:
        text = item[2:]
        children_of_item = text_to_children(text)
        html_items.append(ParentNode('li', children_of_item))
    return ParentNode('ul', html_items)
        

def code_to_html(block):
    if not block.startswith('```') or not block.endswith('```'):
        raise ValueError('bad code block')
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode('code', children)
    return ParentNode('pre', code)

def paragraph_to_html(block):
    lines = block.split('\n')
    paragraph = ' '.join(lines)
    children = text_to_children(paragraph)
    return ParentNode('p', children)
    
def blockquote_to_html(block):
    lines = block.split('\n')
    newlines = []
    for line in lines:
        if not line.startswith('>'):
            raise ValueError('Invalid quote line')
        newlines.append(line.lstrip('>').strip())
        content = " ".join(newlines)
        children = text_to_children(content)
        return ParentNode('blockquote', children)
        
def heading_to_html(block):
    level = 0
    for char in block[:7]:
        if char == '#':
             level+=1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f'bad heading level: {level}')
    text = block[level+1:]
    children = text_to_children(text)
    return ParentNode(f'h{level}', children)

