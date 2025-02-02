from textnode import *
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    result = [node]
    result = split_nodes_delimiter(result, '**', TextType.BOLD)
    result = split_nodes_delimiter(result, '*', TextType.ITALIC)
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result

def markdown_to_blocks(mdtext):
    blocks = mdtext.split("\n\n")
    for block in blocks:
        block.strip()
        if block == '' or block == "\n":
            blocks.remove(block.index())
    return blocks

def block_to_block_type(mdtext):
    if mdtext[0:2] == "```" and mdtext[-3:] == '```':
        return 'code'
    elif mdtext.startswith('>'):
        return 'blockquote'
    elif mdtext.startswith('* ') or mdtext.startswith('- '):
        return 'liu' 
    elif mdtext.startswith('#'):
        if "# " in mdtext[0:6]:
            return 'h'
    elif mdtext.startswith('1. '):
        return 'lio'
    else:
        return 'p'