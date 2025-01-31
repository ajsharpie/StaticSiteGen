from textnode import TextNode, TextType
from htmlnode import *
from random import randint


def main():
    node = LeafNode("img", "imagename.png", {"class": "fit-pic", "src": "google.com", "alt": "hover/caption"}).to_html()
    print(node)

if __name__== "__main__":
    main()

