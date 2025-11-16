import logging
import json
import re
from typing import Dict, Any
from datetime import datetime

def setup_logging():
    """Setup basic logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('story_agent.log')
        ]
    )

def safe_json_parse(json_string: str) -> Dict[str, Any]:
    """Safely parse JSON string, handling common issues"""
    try:
        # Remove markdown code blocks if present
        json_string = re.sub(r'```json\s*|\s*```', '', json_string).strip()
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        logging.error(f"JSON parsing error: {e}")
        # Try to fix common JSON issues
        try:
            # Add missing quotes around keys
            json_string = re.sub(r'(\w+):', r'"\1":', json_string)
            return json.loads(json_string)
        except json.JSONDecodeError:
            logging.error("Failed to parse JSON after cleanup")
            return {}

def generate_timestamp() -> str:
    """Generate a timestamp string"""
    return datetime.now().isoformat()

def validate_story_params(genre: str, premise: str, length: int) -> bool:
    """Validate story generation parameters"""
    if not genre or not premise:
        return False
    if length <= 0 or length > 10000:
        return False
    return True