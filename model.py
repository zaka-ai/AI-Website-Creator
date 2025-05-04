import os
import requests
from dotenv import load_dotenv
from typing import Union

load_dotenv()

class WebGenieModel:
    def __init__(self):
        self.api_url = os.getenv("NGROK_API_URL")  # Load from .env
        self.timeout = int(os.getenv("API_TIMEOUT", "600"))  # Default to 600 if not set
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def call_api(self, prompt: str) -> Union[str, dict]:
        """
        Makes raw API call and returns response
        Args:
            prompt: Complete formatted prompt string
        Returns:
            Raw API response (str or dict)
        Raises:
            RuntimeError: If API call fails
        """
        try:
            if not self.api_url:
                raise ValueError("API URL not configured - check .env file")
                
            response = requests.post(
                self.api_url,
                json={"prompt": prompt},
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            try:
                return response.json()
            except ValueError:
                return response.text

        except requests.exceptions.RequestException as e:
            error_msg = f"API request failed: {str(e)}"
            print(f"[ERROR] {error_msg}")
            raise RuntimeError(error_msg)
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            print(f"[ERROR] {error_msg}")
            raise RuntimeError(error_msg)