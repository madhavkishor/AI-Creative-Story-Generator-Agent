#!/usr/bin/env python3
"""
Alternative entry point for the AI Story Agent
Can be used for different run modes
"""

import argparse
import uvicorn
from src.utils.config import load_config

def run_cli():
    """Run in CLI mode"""
    from src.main import main
    main()

def run_api():
    """Run in API mode"""
    uvicorn.run("src.api.routes:app", host="0.0.0.0", port=8000, reload=True)

def main():
    parser = argparse.ArgumentParser(description="AI Story Agent")
    parser.add_argument(
        "--mode", 
        choices=["cli", "api"], 
        default="cli",
        help="Run mode: cli (command line) or api (web API)"
    )
    
    args = parser.parse_args()
    
    if args.mode == "cli":
        run_cli()
    elif args.mode == "api":
        run_api()

if __name__ == "__main__":
    main()