import json
import os
from typing import List, Dict, Optional
from src.models.story_models import GeneratedStory

class StoryMemory:
    """Manages storage and retrieval of generated stories"""
    
    def __init__(self, config):
        self.config = config
        self.storage_path = config.get('database.path', './data/stories/')
        self._ensure_storage_path()
    
    def _ensure_storage_path(self):
        """Ensure the storage directory exists"""
        os.makedirs(self.storage_path, exist_ok=True)
    
    def store_story(self, story: GeneratedStory):
        """Store a generated story"""
        file_path = os.path.join(self.storage_path, f"{story.story_id}.json")
        with open(file_path, 'w') as file:
            json.dump(story.dict(), file, indent=2, default=str)
    
    def load_story(self, story_id: str) -> Optional[GeneratedStory]:
        """Load a story by ID"""
        file_path = os.path.join(self.storage_path, f"{story_id}.json")
        
        if not os.path.exists(file_path):
            return None
        
        try:
            with open(file_path, 'r') as file:
                story_data = json.load(file)
            
            return GeneratedStory(**story_data)
        except Exception as e:
            print(f"Error loading story {story_id}: {e}")
            return None
    
    def list_stories(self) -> List[Dict[str, str]]:
        """List all stored stories"""
        stories = []
        
        for filename in os.listdir(self.storage_path):
            if filename.endswith('.json'):
                story_id = filename[:-5]  # Remove .json extension
                story = self.load_story(story_id)
                if story:
                    stories.append({
                        'story_id': story_id,
                        'title': story.title,
                        'genre': story.outline.genre,
                        'created_at': story.created_at.isoformat()
                    })
        
        return sorted(stories, key=lambda x: x['created_at'], reverse=True)
    
    def delete_story(self, story_id: str) -> bool:
        """Delete a story by ID"""
        file_path = os.path.join(self.storage_path, f"{story_id}.json")
        
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
    
    def search_stories(self, query: str) -> List[GeneratedStory]:
        """Search stories by content or metadata"""
        # Basic implementation - could be enhanced with vector search
        results = []
        
        for story_info in self.list_stories():
            story = self.load_story(story_info['story_id'])
            if story and (
                query.lower() in story.title.lower() or
                query.lower() in story.outline.premise.lower() or
                query.lower() in story.content.lower()
            ):
                results.append(story)
        
        return results
