#!/usr/bin/env python3
"""
Test runner for AI Story Agent
"""

import os
import sys

# Add current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

def main():
    print("🚀 Testing AI Story Agent...")
    
    try:
        # Import modules
        from src.utils.config import load_config
        from src.utils.helpers import setup_logging
        from src.agents.story_agent import StoryAgent
        
        print("✅ All imports successful!")
        
        # Setup
        setup_logging()
        config = load_config()
        
        print("✅ Configuration loaded!")
        
        # Test API key
        api_key = config.get('openai.api_key')
        if not api_key or api_key == 'your_openai_api_key_here':
            print("❌ Please set your OpenAI API key in .env file")
            return
        
        print("✅ OpenAI API key found!")
        
        # Initialize agent
        story_agent = StoryAgent(config)
        print("✅ Story Agent initialized!")
        
        # Generate a simple story
        print("📖 Generating test story...")
        story = story_agent.generate_story(
            genre="fantasy",
            premise="A young mage discovers a hidden power",
            length=300
        )
        
        print("🎉 Story generated successfully!")
        print(f"Title: {story.title}")
        print(f"Preview: {story.content[:100]}...")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Checking project structure...")
        check_project_structure()
    except Exception as e:
        print(f"❌ Error: {e}")

def check_project_structure():
    """Check if all required files exist"""
    required_files = [
        'src/__init__.py',
        'src/agents/__init__.py',
        'src/agents/story_agent.py',
        'src/utils/__init__.py', 
        'src/utils/config.py',
        'src/utils/helpers.py',
        'src/utils/prompts.py',
        'src/models/__init__.py',
        'src/models/story_models.py',
        'config/default.yaml',
        '.env'
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING")

if __name__ == "__main__":
    main()