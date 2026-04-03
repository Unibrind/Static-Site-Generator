import unittest
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextNodeToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("Click me!", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me!")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_image(self):
        node = TextNode("Alt text", TextType.IMAGE, "https://voldemort.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://voldemort.com/image.png", "alt": "Alt text"},
        )
    
    def test_text_node_to_html_node_image(self):
        node = TextNode("Un titre d'image", TextType.IMAGE, "https://url.com/photo.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://url.com/photo.jpg", "alt": "Un titre d'image"})


if __name__ == "__main__":
    unittest.main()