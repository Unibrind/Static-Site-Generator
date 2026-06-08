def extract_title(markdown):
    lines = markdown.split("\n")
    
    for line in lines:
        cleaned_line = line.strip()
        
        if cleaned_line.startswith("# "):
            return cleaned_line[2:].strip()
            
    raise Exception("No h1 header found in markdown")