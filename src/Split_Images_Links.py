from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextType ,TextNode

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        images = extract_markdown_images(original_text)
        
        if len(images) == 0:
            new_nodes.append(node)
            continue
        
        for image in images:
            alt = image[0]
            link = image[1]
            sections = original_text.split(f"![{alt}]({link})", 1)
        
            if len(sections) != 2:
                raise Exception("Invalid markdown, image section not closed")
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt,TextType.IMAGE, link))
            original_text = sections[1]
        
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    
    return new_nodes


def split_nodes_link(old_nodes):
    
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        original_text = node.text
        links = extract_markdown_links(original_text)
        
        if len(links) == 0:
            new_nodes.append(node)
            continue
        
        for link_tuple in links:
            alt = link_tuple[0]
            link = link_tuple[1]
            sections = original_text.split(f"[{alt}]({link})", 1)
        
            if len(sections) != 2:
                raise Exception("Invalid markdown, link section not closed")
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt,TextType.LINK, link))
            original_text = sections[1]
            original_text = sections[1]
        
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    
    return new_nodes