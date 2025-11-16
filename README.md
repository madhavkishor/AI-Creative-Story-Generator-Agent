# AI Creative Story Generator Agent 
> An intelligent AI-powered story generation system that creates coherent, engaging stories, with consistent characters and plots.

## 🚀 Features  
- **Story Generation**: Generate full narratives from user-provided premises.  
- **Character Development**: Automatically create and evolve detailed character profiles.  
- **Consistency Checking**: Ensure story characters, settings and events remain coherent across chapters.  
- **Multiple Genres**: Fantasy, sci-fi, mystery and more.  
- **REST API**: Web interface for story generation & continuation.  
- **Persistence**: Store, retrieve and continue generated stories.

## 🧠 Why It Exists  
Writing compelling stories—and especially maintaining consistency in characters, world-building and plot across multiple chapters—can be hard.  
This project leverages AI (e.g., large language models) to act as a “story agent” that helps authors, game-writers or hobbyists generate narratives more quickly while keeping them engaging and sensible.

## 📦 Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/madhavkishor/AI_STORY_AGENT.git
   cd AI_STORY_AGENT
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Copy and configure environment variables:

   ```bash
   cp .env.example .env
   # Then edit .env and add your API keys (e.g., OpenAI) and any configuration variables.
   ```

## 🏁 Usage

### ➤ Command Line Interface

```bash
python run.py --mode cli
```

Or directly via the package interface (if installed):

```python
from src.agents.story_agent import StoryAgent
from src.utils.config import load_config

config = load_config()
agent = StoryAgent(config)
story = agent.generate_story(
    genre="fantasy",
    premise="A young mage discovers hidden powers",
    length=1000
)
print(story)
```

### ➤ Web API

You can launch a REST API server:

```bash
python run.py --mode api
```

or using `uvicorn` if the codebase uses FastAPI (for example):

```bash
uvicorn src.api.routes:app --reload
```

#### Example Endpoints

* `POST /generate-story` — Generate a new story.
* `POST /stories/{id}/continue` — Continue an existing story by ID.
* `POST /develop-character` — Create or enhance a character profile.
* `GET /stories` — List all stories.
* `GET /stories/{id}` — Retrieve a specific story.

## ⚙️ Configuration

Configuration settings are located in `config/default.yaml` (or similar). You can tweak:

* Model parameters (e.g., for OpenAI, GPT-4, GPT-3.5)
* Story generation settings (length, temperature, genre options)
* Database / persistence paths
* Logging levels

## 🧩 Project Structure

```
AI_STORY_AGENT/
├─ config/
│   └─ default.yaml
├─ data/
├─ src/
│   ├─ agents/
│   │   └─ story_agent.py
│   ├─ api/
│   │   └─ routes.py
│   ├─ utils/
│   │   ├─ config.py
│   │   └─ …  
│   └─ main.py
├─ tests/
│   └─ test_run.py
├─ .env.example
├─ requirements.txt
├─ setup.py
└─ README.md
```

*(Adjust accordingly to your actual file structure.)*

## ✅ Testing

```bash
pytest tests/
```

## 🔍 Example

Here’s a quick example of how you might use it:

* Genre: **Mystery**
* Premise: *“A detective in a fog-shrouded seaside town uncovers an ancient secret.”*
* Length: **1200 words**
* Output: A multi-chapter story that introduces characters, builds tension, and resolves the mystery—while keeping character motives consistent throughout.

## 🤝 Contributing

Contributions are very welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Make your changes, add tests if applicable.
4. Submit a pull request and describe your changes clearly.


```text
MIT License
Copyright (c) 2025 Madhav Kishor
```

## 📫 Contact

If you have questions, suggestions or want to share your results:

* Email:(mailto:madhavkishor51052l@example.com)
* Twitter/GitHub: [@madhavkishor](https://github.com/madhavkishor)
* Issues: Use the GitHub repository’s “Issues” tab to report bugs or propose enhancements.

