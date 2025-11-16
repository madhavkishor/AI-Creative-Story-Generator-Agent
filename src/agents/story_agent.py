import openai
import json
import uuid
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..models.story_models import StoryOutline, GeneratedStory, StoryGenre, Character, ConsistencyReport
from .character_agent import CharacterAgent
from .consistency_agent import ConsistencyAgent
from ..memory.story_memory import StoryMemory
from ..utils.prompts import StoryPrompts
from ..utils.helpers import safe_json_parse, validate_story_params

class StoryAgent:
    """Main agent responsible for story generation"""
    
    def __init__(self, config):
        self.config = config
        self.llm_client = openai.OpenAI(api_key=config.get('openai.api_key'))
        self.character_agent = CharacterAgent(config)
        self.consistency_agent = ConsistencyAgent(config)
        self.story_memory = StoryMemory(config)
        self.prompts = StoryPrompts()
    
    def generate_story_outline(self, genre: StoryGenre, premise: str) -> StoryOutline:
        """Generate a story outline based on genre and premise"""
        prompt = self.prompts.get_outline_prompt(genre, premise)
        
        try:
            response = self.llm_client.chat.completions.create(
                model=self.config.get('openai.model', 'gpt-3.5-turbo'),
                messages=[{"role": "user", "content": prompt}],
                temperature=0.8,
                max_tokens=self.config.get('openai.max_tokens', 2000)
            )
            
            content = response.choices[0].message.content
            outline_data = safe_json_parse(content)
            
            # Convert to StoryOutline object
            characters = [
                Character(
                    name=char_data.get('name', 'Unknown'),
                    role=char_data.get('role', 'supporting'),
                    background=char_data.get('description', ''),
                    personality=char_data.get('personality_traits', {}),
                    appearance=char_data.get('appearance', ''),
                    relationships=char_data.get('relationships', ''),
                    motivations=char_data.get('motivations', [])
                ) for char_data in outline_data.get('characters', [])
            ]
            
            return StoryOutline(
                title=outline_data.get('title', 'Untitled Story'),
                premise=outline_data.get('premise', premise),
                genre=genre,
                chapters=outline_data.get('chapters', []),
                key_events=outline_data.get('key_events', []),
                characters=characters
            )
            
        except Exception as e:
            print(f"Error generating outline: {e}")
            # Return a basic outline as fallback
            return StoryOutline(
                title="Fallback Story",
                premise=premise,
                genre=genre,
                chapters=[f"Chapter {i+1}" for i in range(5)],
                key_events=["Basic story structure"],
                characters=[]
            )
    
    def generate_story(self, genre: str, premise: str, length: int = 1000) -> GeneratedStory:
        """Generate a complete story"""
        if not validate_story_params(genre, premise, length):
            raise ValueError("Invalid story parameters")
        
        # Create outline
        outline = self.generate_story_outline(StoryGenre(genre), premise)
        
        # Develop characters
        developed_characters = []
        for character in outline.characters:
            developed_char = self.character_agent.develop_character(
                character.dict(), 
                f"Genre: {genre}, Premise: {premise}"
            )
            developed_characters.append(developed_char)
        
        # Generate story content
        story_content = self._generate_content(outline, developed_characters, length)
        
        # Check consistency if enabled
        consistency_report = None
        if self.config.get('agents.consistency.enabled', True):
            consistency_report = self.consistency_agent.check_consistency(
                story_content, outline.dict(), [char.dict() for char in developed_characters]
            )
        
        # Store in memory
        story = GeneratedStory(
            story_id=self._generate_story_id(),
            title=outline.title,
            content=story_content,
            outline=outline,
            metadata={
                "genre": genre,
                "premise": premise,
                "length": length,
                "word_count": len(story_content.split()),
                "consistency_report": consistency_report.dict() if consistency_report else None
            },
            created_at=datetime.now()
        )
        
        self.story_memory.store_story(story)
        
        return story
    
    def _generate_content(self, outline: StoryOutline, characters: List[Character], length: int) -> str:
        """Generate the actual story content"""
        full_story = []
        
        for i, chapter_desc in enumerate(outline.chapters):
            prompt = self.prompts.get_story_content_prompt(
                outline.dict(), 
                [char.dict() for char in characters], 
                i
            )
            
            try:
                response = self.llm_client.chat.completions.create(
                    model=self.config.get('openai.model', 'gpt-3.5-turbo'),
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=min(1500, length // len(outline.chapters))
                )
                
                chapter_content = response.choices[0].message.content
                full_story.append(chapter_content)
                
            except Exception as e:
                print(f"Error generating chapter {i+1}: {e}")
                full_story.append(f"[Chapter {i+1} content could not be generated]")
        
        return "\n\n".join(full_story)
    
    def _generate_story_id(self) -> str:
        """Generate unique story ID"""
        return str(uuid.uuid4())
    
    def continue_story(self, existing_story: GeneratedStory, additional_length: int = 500) -> GeneratedStory:
        """Continue an existing story"""
        # Implementation for continuing stories
        pass
    
    def get_story_by_id(self, story_id: str) -> Optional[GeneratedStory]:
        """Retrieve a story by ID"""
        return self.story_memory.load_story(story_id)