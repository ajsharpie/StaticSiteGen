from textnode import TextNode, TextType
from htmlnode import *
from random import randint


def main():
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
    print(node)

if __name__== "__main__":
    main()

