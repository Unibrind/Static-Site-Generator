from Split_Images_Links import split_nodes_image, split_nodes_link
from split_nodes import split_nodes_delimiter
from textnode import TextType, TextNode

text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    bold = split_nodes_delimiter(new_nodes,"**",TextType.BOLD)
    italic = split_nodes_delimiter(bold,"_",TextType.ITALIC)
    code = split_nodes_delimiter(italic,"`",TextType.CODE)
    image = split_nodes_image(code)
    link = split_nodes_link(image)
    return link

result = text_to_textnodes(text)
print(result)