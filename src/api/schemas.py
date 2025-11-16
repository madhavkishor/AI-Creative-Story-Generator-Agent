from typing import Optional, List
from pydantic import BaseModel, Field
from src.models.story_models import StoryGenre

class StoryRequest(BaseModel):
    genre: StoryGenre = Field(..., description="Story genre")
    premise: str = Field(..., description="Story premise")
    length: int = Field(1000, description="Approximate story length in words")
    enable_consistency_check: bool = Field(True, description="Enable consistency checking")

class StoryResponse(BaseModel):
    story_id: str = Field(..., description="Unique story identifier")
    title: str = Field(..., description="Story title")
    content: str = Field(..., description="Story content")
    outline: dict = Field(..., description="Story outline")
    metadata: dict = Field(..., description="Generation metadata")

class ContinueStoryRequest(BaseModel):
    story_id: str = Field(..., description="ID of story to continue")
    additional_length: int = Field(500, description="Additional length in words")

class CharacterRequest(BaseModel):
    name: str = Field(..., description="Character name")
    role: str = Field(..., description="Character role")
    description: str = Field(..., description="Character description")
    story_context: str = Field(..., description="Story context for character development")

class CharacterResponse(BaseModel):
    character: dict = Field(..., description="Developed character profile")

class ErrorResponse(BaseModel):
    error: str = Field(..., description="Error message")
    details: Optional[str] = Field(None, description="Error details")