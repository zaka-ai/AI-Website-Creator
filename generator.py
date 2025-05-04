from model import WebGenieModel
from utils.parser import parse_code_blocks
from prompt import PROMPT_TEMPLATE
from typing import Dict, Optional, Union

class WebsiteGenerator:
    def __init__(self):
        self.model = WebGenieModel()

    def generate_website(self, config: Dict) -> Optional[Dict]:
        """
        Complete website generation workflow
        Args:
            config: User configuration dictionary containing:
                - description
                - primary_color
                - secondary_color  
                - font_family
                - layout_style
                - include_animation
                - dark_mode
                - num_sections
        Returns:
            Dictionary with parsed code blocks:
                {
                    "html": "...",
                    "css": "...",
                    "javascript": "..."
                }
            or None if generation fails
        """
        try:
            # Step 1: Create formatted prompt
            prompt = self._create_prompt(config)
            print(f"[DEBUG] Generated prompt: {prompt[:200]}...")  # Log first 200 chars
            
            # Step 2: Call API
            raw_response = self.model.call_api(prompt)
            print(f"[DEBUG] Raw API response: {str(raw_response)}")
            
            # Step 3: Parse response
            response_text = self._extract_response_text(raw_response)
            if not response_text:
                raise ValueError("Empty response from API")
                
            # Step 4: Parse code blocks
            code_blocks = parse_code_blocks(response_text)
            if not code_blocks:
                raise ValueError("No valid code blocks found")
                
            return code_blocks
            
        except Exception as e:
            print(f"[ERROR] Generation failed: {str(e)}")
            return None

    def _create_prompt(self, config: Dict) -> str:
        """Formats the prompt using the template"""
        return PROMPT_TEMPLATE.format(
            description=config["description"],
            primary_color=config.get("primary_color", "#4F46E5"),
            secondary_color=config.get("secondary_color", "#10B981"),
            font_family=config.get("font_family", "Inter"),
            layout_style=config.get("layout_style", "Modern"),
            include_animation="Yes" if config.get("include_animation", False) else "No",
            dark_mode="Yes" if config.get("dark_mode", False) else "No",
            num_sections=config.get("num_sections", 3)
        )

    def _extract_response_text(self, raw_response: Union[str, dict]) -> str:
        """Extracts response text from API response"""
        if isinstance(raw_response, dict):
            return raw_response.get("response", "").strip()
        return str(raw_response).strip()