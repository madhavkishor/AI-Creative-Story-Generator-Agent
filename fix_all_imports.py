#!/usr/bin/env python3
"""
Fix all import issues in the project
"""

import os
import re

def fix_imports_in_file(file_path):
    """Fix import statements in a file"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Fix patterns
    fixes = [
        # Remove src. from imports
        (r'from src\.models\.', r'from ..models.'),
        (r'from src\.utils\.', r'from ..utils.'),
        (r'from src\.agents\.', r'from .'),
        (r'from src\.memory\.', r'from ..memory.'),
        (r'from src\.config\.', r'from ..config.'),
        (r'from src\.api\.', r'from ..api.'),
        # Add json import if needed in prompts.py
        (r'from typing import List, Dict, Any\nfrom \.\.models\.story_models import StoryGenre', 
         r'import json\nfrom typing import List, Dict, Any\nfrom ..models.story_models import StoryGenre'),
    ]
    
    original_content = content
    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content)
    
    if content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"✅ Fixed imports in {file_path}")
        return True
    else:
        print(f"✅ No changes needed for {file_path}")
        return False

def main():
    print("🔧 Fixing all import statements...")
    
    files_to_check = [
        'src/agents/story_agent.py',
        'src/agents/character_agent.py',
        'src/agents/consistency_agent.py', 
        'src/utils/prompts.py',
        'src/utils/config.py',
        'src/utils/helpers.py',
        'src/memory/story_memory.py',
    ]
    
    fixed_count = 0
    for file_path in files_to_check:
        if os.path.exists(file_path):
            if fix_imports_in_file(file_path):
                fixed_count += 1
    
    print(f"\n🎉 Fixed {fixed_count} files")
    print("Now try running: python test_run.py")

if __name__ == "__main__":
    main()