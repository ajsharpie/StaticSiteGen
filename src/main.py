from textnode import TextNode, TextType


def main():
    test_ob = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(test_ob)

if __name__== "__main__":
    main()

