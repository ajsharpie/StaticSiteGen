from textnode import *
import re

def split_nodes_delimiter(old_nodes, delim, type):
    new_nodes = []
    for node in old_nodes:
        if node.type != TextType.TEXT:
            new_nodes.append(node)
            continue
        final_list = []
        lst = node.text.split(delim)
        if len(lst) % 2 == 0:
            raise ValueError("Bad Markdown, not closed")
        for i in range(len(lst)):
            if lst[i] == "":
                continue
            if i % 2 == 0:
                final_list.append(TextNode(lst[i], TextType.TEXT))
            else:
                final_list.append(TextNode(lst[i], type))
        
        new_nodes.extend(final_list)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
            continue
        final_list = []
        before_link = node.text.split(f'[{links[0][0]}]({links[0][1]})', 1)[0]
        after_link = node.text.partition(f'[{links[0][0]}]({links[0][1]})')[2]
        final_list.append(TextNode(before_link, TextType.TEXT))
        final_list.append(TextNode(links[0][0], TextType.LINK, links[0][1]))
        if after_link != '':
            final_list.extend(split_nodes_link([TextNode(after_link, TextType.TEXT)]))  
        new_nodes.extend(final_list)
    return new_nodes
            

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        imgs = extract_markdown_images(node.text)
        if node.text == '':
            return []
        if imgs == []:
            new_nodes.append(node)
            continue
        final_list = []
        before_img = node.text.split(f'![{imgs[0][0]}]({imgs[0][1]})', 1)[0]
        after_img = node.text.partition(f'![{imgs[0][0]}]({imgs[0][1]})')[2]
        final_list.append(TextNode(before_img, TextType.TEXT))
        final_list.append(TextNode('', TextType.IMAGE, {'src': imgs[0][1], 'alt': imgs[0][0]}))
        if after_img != "":
            final_list.extend(split_nodes_image([TextNode(after_img, TextType.TEXT)]))  
        new_nodes.extend(final_list)
    return new_nodes

def extract_markdown_links(md_text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", md_text)
    
def extract_markdown_images(md_text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", md_text)