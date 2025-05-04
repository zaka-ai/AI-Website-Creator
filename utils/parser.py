import re
from typing import Dict, Optional

def parse_code_blocks(markdown_text: str) -> Optional[Dict[str, str]]:
    """
    Parse markdown text to extract code blocks
    
    Args:
        markdown_text: String containing markdown with code blocks
        
    Returns:
        Dictionary with 'html', 'css', and 'javascript' keys
        or None if parsing fails
    """
    code_blocks = {
        "html": "",
        "css": "",
        "javascript": ""
    }
    
    # Pattern to match code blocks with language specification
    pattern = r"```(html|css|javascript)\n(.*?)\n```"
    matches = re.finditer(pattern, markdown_text, re.DOTALL)
    
    for match in matches:
        language = match.group(1).lower()
        code = match.group(2).strip()
        if language in code_blocks:
            code_blocks[language] = code
    
    # Validate we got at least HTML
    if not code_blocks["html"]:
        return None
        
    return code_blocks