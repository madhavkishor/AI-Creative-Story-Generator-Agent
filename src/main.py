#!/usr/bin/env python3
"""
Main entry point for the AI Story Agent
"""

import os
import sys
import logging

# Add the parent directory to Python path so we can import src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from src.agents.story_agent import StoryAgent
    from src.utils.config import load_config
    from src.utils.helpers import setup_logging
except ImportError as e:
    print(f"Import error: {e}")
    print("Trying alternative import structure...")
    # Try relative imports
    from agents.story_agent import StoryAgent
    from utils.config import load_config
    from utils.helpers import setup_logging

def main():
    """Main function to run the story agent"""
    # Setup logging
    setup_logging()
    
    # Load configuration
    config = load_config()
    
    # Initialize story agent
    story_agent = StoryAgent(config)
    
    # Example usage
    print("🤖 AI Story Agent Starting...")
    print("📖 Generating fantasy story...")
    
    story = story_agent.generate_story(
        genre="fantasy",
        premise="A young mage discovers a hidden power",
        length=500  # Reduced for testing
    )
    
    print(f"✅ Story Generated Successfully!")
    print(f"📖 Title: {story.title}")
    print(f"📝 Content Preview: {story.content[:200]}...")
    print(f"🆔 Story ID: {story.story_id}")
    print(f"💾 Story saved to: data/stories/{story.story_id}.json")

if __name__ == "__main__":
    main()