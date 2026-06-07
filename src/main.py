import os
import shutil
from textnode import TextType, TextNode

def copy_static_recursive(source_dir, dest_dir):
    # Si le dossier de destination n'existe pas, on le crée
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
        
    # On liste tout ce qui se trouve dans le dossier source
    for item in os.listdir(source_dir):
        # On crée les chemins complets
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        print(f"Copie en cours : {source_path} -> {dest_path}")
        
        # S'il s'agit d'un fichier, on le copie directement
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        # S'il s'agit d'un dossier, la magie de la récursivité opère !
        else:
            copy_static_recursive(source_path, dest_path)

def main():
    # --- Étape 1 : Ta petite vérification TextNode ---
    print("--- Test TextNode ---")
    node = TextNode("This is some anchor text", TextType.BOLD, "https://www.boot.dev")
    print(node)
    print("---------------------\n")

    # --- Étape 2 : Le Générateur Statique (Copie) ---
    source = "static"
    destination = "public"
    
    # On nettoie d'abord le dossier public s'il existe déjà
    if os.path.exists(destination):
        print(f"Nettoyage du dossier {destination}...")
        shutil.rmtree(destination)
        
    # On lance la copie récursive
    print(f"Début de la copie de {source} vers {destination}...")
    copy_static_recursive(source, destination)
    print("Copie terminée avec succès !")

# C'est le seul et unique point d'entrée du script !
if __name__ == "__main__":
    main()