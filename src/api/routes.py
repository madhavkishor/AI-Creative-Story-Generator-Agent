from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.api.schemas import (
    StoryRequest, StoryResponse, ContinueStoryRequest, 
    CharacterRequest, CharacterResponse, ErrorResponse
)
from src.agents.story_agent import StoryAgent
from src.agents.character_agent import CharacterAgent
from src.utils.config import load_config

app = FastAPI(title="AI Story Agent API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agents
config = load_config()
story_agent = StoryAgent(config)
character_agent = CharacterAgent(config)

@app.post("/generate-story", response_model=StoryResponse, responses={400: {"model": ErrorResponse}})
async def generate_story(request: StoryRequest):
    """Generate a new story"""
    try:
        story = story_agent.generate_story(
            genre=request.genre,
            premise=request.premise,
            length=request.length
        )
        
        return StoryResponse(
            story_id=story.story_id,
            title=story.title,
            content=story.content,
            outline=story.outline.dict(),
            metadata=story.metadata
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/stories/{story_id}/continue", response_model=StoryResponse)
async def continue_story(story_id: str, request: ContinueStoryRequest):
    """Continue an existing story"""
    try:
        existing_story = story_agent.get_story_by_id(story_id)
        if not existing_story:
            raise HTTPException(status_code=404, detail="Story not found")
        
        continued_story = story_agent.continue_story(
            existing_story, 
            request.additional_length
        )
        
        return StoryResponse(
            story_id=continued_story.story_id,
            title=continued_story.title,
            content=continued_story.content,
            outline=continued_story.outline.dict(),
            metadata=continued_story.metadata
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/develop-character", response_model=CharacterResponse)
async def develop_character(request: CharacterRequest):
    """Develop a character profile"""
    try:
        character_data = {
            "name": request.name,
            "role": request.role,
            "description": request.description
        }
        
        character = character_agent.develop_character(
            character_data, 
            request.story_context
        )
        
        return CharacterResponse(character=character.dict())
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/stories")
async def list_stories():
    """List all generated stories"""
    try:
        stories = story_agent.story_memory.list_stories()
        return {"stories": stories}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/stories/{story_id}")
async def get_story(story_id: str):
    """Get a specific story by ID"""
    try:
        story = story_agent.get_story_by_id(story_id)
        if not story:
            raise HTTPException(status_code=404, detail="Story not found")
        return story.dict()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "AI Story Agent API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)