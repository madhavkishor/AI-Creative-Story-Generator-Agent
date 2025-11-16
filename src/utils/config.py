import os
import yaml
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration management for the story agent"""
    
    def __init__(self, config_path: str = None):
        self.config = self._load_config(config_path)
    
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        if config_path is None:
            config_path = os.path.join(
                os.path.dirname(__file__), 
                '../../config/default.yaml'
            )
        
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        
        # Override with environment variables
        config['openai']['api_key'] = os.getenv('OPENAI_API_KEY', '')
        config['database']['path'] = os.getenv('DATABASE_PATH', config['database']['path'])
        
        return config
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

def load_config(config_path: str = None) -> Config:
    """Load configuration"""
    return Config(config_path)