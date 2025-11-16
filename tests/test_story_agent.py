import pytest
import os
from src.agents.story_agent import StoryAgent
from src.utils.config import load_config

class TestStoryAgent:
    @pytest.fixture
    def story_agent(self):
        config = load_config()
        return StoryAgent(config)
    
    def test_generate_story_outline(self, story_agent):
        outline = story_agent.generate_story_outline("fantasy", "A young mage discovers magic")
        
        assert outline.title is not None
        assert outline.premise is not None
        assert len(outline.chapters) > 0
        assert len(outline.characters) >= 0
    
    def test_generate_story(self, story_agent):
        story = story_agent.generate_story(
            genre="fantasy",
            premise="A test story premise",
            length=500
        )
        
        assert story.story_id is not None
        assert story.title is not None
        assert len(story.content) > 0
        assert story.outline is not None
    
    def test_invalid_parameters(self, story_agent):
        with pytest.raises(ValueError):
            story_agent.generate_story("", "Valid premise", 1000)
        
        with pytest.raises(ValueError):
            story_agent.generate_story("fantasy", "", 1000)
        
        with pytest.raises(ValueError):
            story_agent.generate_story("fantasy", "Valid premise", -100)