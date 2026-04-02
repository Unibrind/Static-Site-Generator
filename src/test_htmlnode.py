import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase): # On hérite de TestCase
    def test_props_to_html(self):
        # On crée un vrai objet HTMLNode
        node = HTMLNode("a", "Google", None, {"href": "https://google.com"})
        # On vérifie que sa méthode renvoie le bon texte
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')

    def test_values(self):
        # Test avec des valeurs None
        node = HTMLNode("p", "Hello")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_repr(self):
        # Test que le __repr__ renvoie bien une chaîne de caractères
        node = HTMLNode("h1", "Titre")
        self.assertTrue(node.__repr__().startswith("HTMLNode(h1, Titre"))

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">Click me!</a>')
    
    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()