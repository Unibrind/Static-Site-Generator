def markdown_to_blocks(markdown):
    splited_md = markdown.split("\n\n")
    filtred_block = []
    
    for block in splited_md:
        clean_block = block.strip()
        
        if clean_block != "":
            filtred_block.append(clean_block)
        
    return filtred_block