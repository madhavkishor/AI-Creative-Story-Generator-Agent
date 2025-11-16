import json
from typing import List, Dict, Any

class StoryPrompts:
    @staticmethod
    def get_outline_prompt(genre: str, premise: str) -> str:
        return f"""Create a story outline for a {genre} story with premise: {premise}
        
        Return JSON with: title, premise, chapters, key_events, characters
        """
    
    @staticmethod
    def get_character_prompt(character_info: Dict[str, Any], story_context: str) -> str:
        return f"""Develop this character: {character_info}
        Story context: {story_context}
        Return JSON character profile.
        """
    
    @staticmethod
    def get_story_content_prompt(outline: Dict[str, Any], characters: List[Dict], current_chapter: int = 0) -> str:
        return f"""Write story content for chapter {current_chapter + 1}
        Outline: {outline}
        Characters: {characters}
        """
    
    @staticmethod
    def get_consistency_prompt(story_content: str, outline: Dict[str, Any], characters: List[Dict]) -> str:
        return f"""Check consistency between story and outline.
        Story: {story_content}
        Outline: {outline}
        Characters: {characters}
        Return JSON analysis.
        """
