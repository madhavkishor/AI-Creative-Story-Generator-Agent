# AI Story Agent

An intelligent AI-powered story generation system that creates coherent, engaging stories with consistent characters and plots.

## Features

- **Story Generation**: Generate complete stories from premises
- **Character Development**: Create detailed character profiles
- **Consistency Checking**: Maintain narrative consistency
- **Multiple Genres**: Support for fantasy, sci-fi, mystery, and more
- **REST API**: Web interface for story generation
- **Persistence**: Store and retrieve generated stories

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-story-agent
Install dependencies:

bash
pip install -r requirements.txt
Set up environment variables:

bash
cp .env.example .env
# Edit .env with your OpenAI API key
Usage
Command Line Interface
bash
python src/main.py
Web API
bash
python run.py --mode api
# or
uvicorn src.api.routes:app --reload
As a Python Package
python
from src.agents.story_agent import StoryAgent
from src.utils.config import load_config

config = load_config()
agent = StoryAgent(config)

story = agent.generate_story(
    genre="fantasy",
    premise="A young mage discovers hidden powers",
    length=1000
)
API Endpoints
POST /generate-story - Generate a new story

POST /stories/{id}/continue - Continue an existing story

POST /develop-character - Develop a character profile

GET /stories - List all stories

GET /stories/{id} - Get a specific story

Configuration
Edit config/default.yaml to customize:

OpenAI model settings

Story generation parameters

Database paths

Logging levels

Testing
bash
pytest tests/
Project Structure
See the main README for detailed project structure.

text

## 15. Package Initialization Files

### `src/__init__.py`

```python
"""
AI Story Agent - An intelligent story generation system
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"