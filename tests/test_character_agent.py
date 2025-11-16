import pytest
from src.agents.character_agent import CharacterAgent
from src.utils.config import load_config

class TestCharacterAgent:
    @pytest.fixture
    def character_agent(self):
        config = load_config()
        return CharacterAgent(config)
    
    def test_develop_character(self, character_agent):
        character_data = {
            "name": "Test Character",
            "role": "protagonist",
            "description": "A brave hero"
        }
        
        character = character_agent.develop_character(
            character_data, 
            "A fantasy adventure story"
        )
        
        assert character.name == "Test Character"
        assert character.role == "protagonist"
        assert character.background is not None