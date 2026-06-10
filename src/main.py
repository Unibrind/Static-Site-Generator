import os
import shutil
from textnode import TextType, TextNode
from generate_pages_recursive import generate_pages_recursive
def copy_static_recursive(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
        
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        print(f"Copie en cours : {source_path} -> {dest_path}")
        
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            copy_static_recursive(source_path, dest_path)

def main():
    print("--- Test TextNode ---")
    node = TextNode("This is some anchor text", TextType.BOLD, "https://www.boot.dev")
    print(node)
    print("---------------------\n")

    source = "static"
    destination = "public"
    
    if os.path.exists(destination):
        print(f"Nettoyage du dossier {destination}...")
        shutil.rmtree(destination)
        
    print(f"Début de la copie de {source} vers {destination}...")
    copy_static_recursive(source, destination)
    print("Copie terminée avec succès !")
    
    print("\nGénération de toutes les pages du site...")
    generate_pages_recursive("content", "template.html", "public")
    
    print("\nTout le site web a été généré avec succès !")

if __name__ == "__main__":
    main()