from markdown_to_blocks import markdown_to_blocks
from Block_Types import block_to_block_type, BlockType
from htmlnode import LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_children = []
    
    for text_node in text_nodes:
        html_children.append(text_node_to_html_node(text_node))
    return html_children


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.HEADING:
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break
            
            text = block[level + 1:]
            node = ParentNode(f"h{level}", text_to_children(text))
            children.append(node)
        
        
        elif block_type == BlockType.CODE:
            text = block.strip("```").strip("\n")
            code_leaf = LeafNode("code", text)
            node = ParentNode("pre", [code_leaf])
            children.append(node)
        
        
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned_lines = []
            for line in lines:
                cleaned_lines.append(line.lstrip(">").strip())
            text = " ".join(cleaned_lines)
            node = ParentNode("blockquote", text_to_children(text))
            children.append(node)
        
        
        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            list_items = []
            for line in lines:
                text = line[2:]
                list_items.append(ParentNode("li", text_to_children(text)))
            node = ParentNode("ul", list_items)
            children.append(node)
        
        
        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            list_items = []
            for line in lines:
                space_index = line.find(" ")
                text = line[space_index + 1:]
                list_items.append(ParentNode("li", text_to_children(text)))
            node = ParentNode("ol", list_items)
            children.append(node)
            
            
        else:
            text = " ".join(block.split("\n"))
            node = ParentNode("p", text_to_children(text))
            children.append(node)
            
            
    return ParentNode("div", children)