from textnode import TextType ,TextNode

def main():
    node = TextNode("This is some anchor text", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()