import unittest
from textnode import TextNode, TextType
# Assure-toi que le nom après "from" est bien le nom de ton fichier .py
from Split_Images_Links import split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):
    def test_split_image(self):
        node = TextNode(
            "Ceci est une ![image](https://i.imgur.com/zjjcJKZ.png) et une autre ![seconde](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Ceci est une ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" et une autre ", TextType.TEXT),
                TextNode("seconde", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![seule](https://www.example.com/image.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("seule", TextType.IMAGE, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "Clique ici [Google](https://www.google.com) ou [Boot dev](https://www.boot.dev) pour apprendre.",
            TextType.TEXT,
        )
        # Ici on appelle bien split_nodes_link
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Clique ici ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
                TextNode(" ou ", TextType.TEXT),
                TextNode("Boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" pour apprendre.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_no_links_or_images(self):
        node = TextNode("Texte simple sans rien.", TextType.TEXT)
        self.assertListEqual([node], split_nodes_link([node]))
        self.assertListEqual([node], split_nodes_image([node]))

if __name__ == "__main__":
    unittest.main()