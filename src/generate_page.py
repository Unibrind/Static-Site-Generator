import os
from markdown_to_html_node import markdown_to_html_node
from extract_title_markdown import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, mode='r', encoding="utf-8") as f:
        markdown_content = f.read()
        
    with open(template_path, mode='r', encoding="utf-8") as f:
        template_content = f.read()
    
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    title = extract_title(markdown_content)
    
    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
        
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)
