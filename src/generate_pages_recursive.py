import os
from markdown_to_html_node import markdown_to_html_node # Assure-toi d'importer tes fonctions
from extract_title_markdown import extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, entry)
        
        if os.path.isfile(from_path):
            if entry.endswith(".md"):
                dest_filename = entry.replace(".md", ".html")
                dest_path = os.path.join(dest_dir_path, dest_filename)
                
                print(f"Generating page from {from_path} to {dest_path} using {template_path}")
                
                with open(from_path, "r", encoding="utf-8") as f:
                    markdown_content = f.read()
                with open(template_path, "r", encoding="utf-8") as f:
                    template_content = f.read()
                
                html_node = markdown_to_html_node(markdown_content)
                html_content = html_node.to_html()
                
                title = extract_title(markdown_content)
                
                final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
                
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                
                with open(dest_path, "w", encoding="utf-8") as f:
                    f.write(final_html)
                    
        else:
            new_dest_dir = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(from_path, template_path, new_dest_dir)