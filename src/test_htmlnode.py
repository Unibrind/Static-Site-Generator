import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()