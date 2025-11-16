#!/usr/bin/env python3
"""
Find files that have bad import statements
"""

import os
import re

def find_bad_imports():
    print("🔍 Searching for bad import statements...")
    
    bad_imports_found = False
    
    # Check all Python files
    for root, dirs, files in os.walk('src'):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Look for src.config imports
                if re.search(r'from src\.config|import src\.config', content):
                    print(f"❌ Found src.config import in: {file_path}")
                    bad_imports_found = True
                
                # Look for other src. imports that should be relative
                src_imports = re.findall(r'from src\.\w+', content)
                if src_imports:
                    print(f"⚠️  Found src.* imports in {file_path}: {src_imports}")
                    bad_imports_found = True
    
    if not bad_imports_found:
        print("✅ No bad imports found!")
    
    return bad_imports_found

def check_all_files_content():
    """Check content of key files"""
    print("\n📄 Checking key files content...")
    
    files_to_check = [
        'src/utils/config.py',
        'src/agents/story_agent.py',
        'src/agents/character_agent.py',
        'src/agents/consistency_agent.py',
        'src/utils/prompts.py'
    ]
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            print(f"\n--- {file_path} ---")
            with open(file_path, 'r') as f:
                lines = f.readlines()
                # Show first 10 lines
                for i, line in enumerate(lines[:10]):
                    print(f"{i+1}: {line.rstrip()}")
        else:
            print(f"❌ {file_path} not found")

if __name__ == "__main__":
    find_bad_imports()
    check_all_files_content()