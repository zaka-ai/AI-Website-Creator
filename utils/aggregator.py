def combine_code(html: str, css: str, js: str) -> str:
    """
    Combine HTML, CSS, and JS into a single HTML string
    
    Args:
        html: HTML code
        css: CSS code
        js: JavaScript code
        
    Returns:
        Combined HTML string with embedded CSS and JS
    """
    # Insert CSS into head
    if css:
        css_tag = f"<style>{css}</style>"
        if "<head>" in html:
            html = html.replace("</head>", f"{css_tag}</head>")
        else:
            html = f"{css_tag}{html}"
    
    # Insert JS before body close
    if js:
        js_tag = f"<script>{js}</script>"
        if "<body>" in html:
            html = html.replace("</body>", f"{js_tag}</body>")
        else:
            html = f"{html}{js_tag}"
    
    return html