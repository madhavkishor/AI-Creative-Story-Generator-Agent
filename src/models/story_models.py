from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class StoryGenre(str, Enum):
    FANTASY = "fantasy"
    SCI_FI = "sci_fi"
    MYSTERY = "mystery"
    ROMANCE = "romance"
    HORROR = "horror"
    ADVENTURE = "adventure"
    CONTEMPORARY = "contemporary"

class StoryElement(BaseModel):
    """Represents a story element (character, location, event)"""
    element_type: str = Field(..., description="Type of element: character, location, object, etc.")
    name: str = Field(..., description="Name of the element")
    description: str = Field(..., description="Detailed description")
    attributes: Dict[str, Any] = Field(default_factory=dict, description="Additional attributes")

class Character(BaseModel):
    """Detailed character model"""
    name: str = Field(..., description="Character's full name")
    role: str = Field(..., description="protagonist, antagonist, supporting, etc.")
    background: str = Field(..., description="Character backstory")
    personality: Dict[str, Any] = Field(..., description="Personality traits and characteristics")
    appearance: str = Field(..., description="Physical description")
    relationships: str = Field(..., description="Relationships with other characters")
    motivations: List[str] = Field(default_factory=list, description="Character motivations")

class StoryOutline(BaseModel):
    """Story outline structure"""
    title: str = Field(..., description="Story title")
    premise: str = Field(..., description="Story premise")
    genre: StoryGenre = Field(..., description="Story genre")
    chapters: List[str] = Field(..., description="Chapter summaries")
    key_events: List[str] = Field(..., description="Key plot events")
    characters: List[Character] = Field(default_factory=list, description="Main characters")

class GeneratedStory(BaseModel):
    """Complete generated story"""
    story_id: str = Field(..., description="Unique story identifier")
    title: str = Field(..., description="Story title")
    content: str = Field(..., description="Full story content")
    outline: StoryOutline = Field(..., description="Story outline")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Generation metadata")
    created_at: datetime = Field(default_factory=datetime.now, description="Creation timestamp")

class ConsistencyReport(BaseModel):
    """Consistency check report"""
    is_consistent: bool = Field(..., description="Overall consistency status")
    issues: List[Dict[str, Any]] = Field(default_factory=list, description="Identified issues")
    overall_feedback: str = Field(..., description="General feedback")