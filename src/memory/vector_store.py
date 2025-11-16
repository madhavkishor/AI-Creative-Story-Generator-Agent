import chromadb
import os
from typing import List, Dict, Any
from src.models.story_models import GeneratedStory

class VectorStore:
    """Vector database for semantic story search"""
    
    def __init__(self, config):
        self.config = config
        self.persistence_path = config.get('database.vector_store', './data/vector_store')
        self.client = chromadb.PersistentClient(path=self.persistence_path)
        self.collection = self.client.get_or_create_collection(name="stories")
    
    def add_story(self, story: GeneratedStory):
        """Add a story to the vector store"""
        self.collection.add(
            documents=[story.content],
            metadatas=[{
                "story_id": story.story_id,
                "title": story.title,
                "genre": story.outline.genre,
                "premise": story.outline.premise
            }],
            ids=[story.story_id]
        )
    
    def search_similar_stories(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """Search for similar stories using semantic search"""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        return [
            {
                "story_id": results['ids'][0][i],
                "metadata": results['metadatas'][0][i],
                "distance": results['distances'][0][i] if results['distances'] else None
            }
            for i in range(len(results['ids'][0]))
        ]
    
    def delete_story(self, story_id: str):
        """Delete a story from the vector store"""
        self.collection.delete(ids=[story_id])