from markdown_to_html_node import markdown_to_html_node

print("Mon script de debug se lance enfin !")

print("--- DIAGNOSTIC DE TO_HTML ---")
try:
    test_md = "# Mon Titre\n\nUn paragraphe de texte."
    node = markdown_to_html_node(test_md)
    print(f"Type du nœud retourné : {type(node)}")
    
    html_string = node.to_html()
    print("Résultat de .to_html() :")
    print(html_string)
except Exception as e:
    print(f"❌ Erreur pendant l'exécution : {e}")