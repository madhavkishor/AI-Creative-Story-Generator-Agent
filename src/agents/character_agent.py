import openai
import json
from typing import List, Dict, Any
from ..models.story_models import Character
from ..utils.prompts import StoryPrompts
from ..utils.helpers import safe_json_parse

class CharacterAgent:
    """Manages character creation and development"""
    
    def __init__(self, config):
        self.config = config
        self.llm_client = openai.OpenAI(api_key=config.get('openai.api_key'))
        self.prompts = StoryPrompts()
    
    def generate_characters(self, outline: Dict[str, Any]) -> List[Character]:
        """Generate characters for a story outline"""
        characters = []
        
        for char_data in outline.get('characters', []):
            developed_char = self.develop_character(char_data, outline.get('premise', ''))
            characters.append(developed_char)
        
        return characters
    
    def develop_character(self, character: Dict[str, Any], story_context: str) -> Character:
        """Develop a character based on story context"""
        prompt = self.prompts.get_character_prompt(character, story_context)
        
        try:
            response = self.llm_client.chat.completions.create(
                model=self.config.get('openai.model', 'gpt-3.5-turbo'),
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1000
            )
            
            content = response.choices[0].message.content
            char_data = safe_json_parse(content)
            
            return Character(
                name=char_data.get('name', character.get('name', 'Unknown')),
                role=char_data.get('role', character.get('role', 'supporting')),
                background=char_data.get('background', ''),
                personality=char_data.get('personality', {}),
                appearance=char_data.get('appearance', ''),
                relationships=char_data.get('relationships', ''),
                motivations=char_data.get('motivations', [])
            )
            
        except Exception as e:
            print(f"Error developing character {character.get('name', 'Unknown')}: {e}")
            # Return basic character as fallback
            return Character(
                name=character.get('name', 'Unknown Character'),
                role=character.get('role', 'supporting'),
                background=character.get('description', 'Basic character'),
                personality={},
                appearance='Not specified',
                relationships='Not specified',
                motivations=[]
            )
    
    def analyze_character_arc(self, character: Character, story_development: str) -> Dict[str, Any]:
        """Analyze how a character develops through the story"""
        # Implementation for character arc analysis
        pass
    
    def generate_character_dialogue(self, character: Character, situation: str) -> str:
        """Generate dialogue for a character in a specific situation"""
        # Implementation for dialogue generation
        pass