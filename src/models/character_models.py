from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from enum import Enum

class CharacterRole(str, Enum):
    PROTAGONIST = "protagonist"
    ANTAGONIST = "antagonist"
    SUPPORTING = "supporting"
    MINOR = "minor"

class PersonalityTrait(str, Enum):
    BRAVE = "brave"
    INTELLIGENT = "intelligent"
    FUNNY = "funny"
    MYSTERIOUS = "mysterious"
    AMBITIOUS = "ambitious"
    LOYAL = "loyal"
    CYNICAL = "cynical"
    OPTIMISTIC = "optimistic"

class CharacterProfile(BaseModel):
    """Comprehensive character profile"""
    name: str = Field(..., description="Character name")
    role: CharacterRole = Field(..., description="Character role in story")
    age: Optional[int] = Field(None, description="Character age")
    background: str = Field(..., description="Character history and background")
    personality_traits: List[PersonalityTrait] = Field(..., description="Key personality traits")
    motivations: List[str] = Field(..., description="Character motivations and goals")
    flaws: List[str] = Field(..., description="Character flaws and weaknesses")
    strengths: List[str] = Field(..., description="Character strengths and abilities")
    appearance: str = Field(..., description="Physical appearance description")
    voice_style: str = Field(..., description="How the character speaks")
    relationships: Dict[str, str] = Field(default_factory=dict, description="Relationships with other characters")
    character_arc: str = Field(..., description="How the character changes through the story")

class CharacterRelationship(BaseModel):
    """Relationship between two characters"""
    character_a: str = Field(..., description="First character name")
    character_b: str = Field(..., description="Second character name")
    relationship_type: str = Field(..., description="Type of relationship")
    description: str = Field(..., description="Relationship description")
    dynamics: List[str] = Field(..., description="Relationship dynamics")