import openai
import json
from typing import List, Dict, Any
from ..models.story_models import ConsistencyReport
from ..utils.prompts import StoryPrompts
from ..utils.helpers import safe_json_parse

class ConsistencyAgent:
    """Ensures narrative consistency throughout the story"""
    
    def __init__(self, config):
        self.config = config
        self.llm_client = openai.OpenAI(api_key=config.get('openai.api_key'))
        self.prompts = StoryPrompts()
    
    def check_consistency(self, story_content: str, outline: Dict[str, Any], 
                         characters: List[Dict]) -> ConsistencyReport:
        """Check story for consistency issues"""
        prompt = self.prompts.get_consistency_prompt(story_content, outline, characters)
        
        try:
            response = self.llm_client.chat.completions.create(
                model=self.config.get('openai.model', 'gpt-3.5-turbo'),
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=1000
            )
            
            content = response.choices[0].message.content
            report_data = safe_json_parse(content)
            
            return ConsistencyReport(
                is_consistent=report_data.get('is_consistent', True),
                issues=report_data.get('issues', []),
                overall_feedback=report_data.get('overall_feedback', 'No issues found')
            )
            
        except Exception as e:
            print(f"Error checking consistency: {e}")
            return ConsistencyReport(
                is_consistent=True,
                issues=[],
                overall_feedback="Consistency check failed due to error"
            )
    
    def fix_inconsistencies(self, story_content: str, issues: List[Dict]) -> str:
        """Fix identified inconsistencies in the story"""
        if not issues:
            return story_content
        
        fix_prompt = f"""
        The following story has consistency issues that need to be fixed:
        
        ORIGINAL STORY:
        {story_content}
        
        IDENTIFIED ISSUES:
        {json.dumps(issues, indent=2)}
        
        Please rewrite the story to fix these issues while maintaining the original style, plot, and characterizations.
        Return only the fixed story content without any additional commentary.
        """
        
        try:
            response = self.llm_client.chat.completions.create(
                model=self.config.get('openai.model', 'gpt-3.5-turbo'),
                messages=[{"role": "user", "content": fix_prompt}],
                temperature=0.5,
                max_tokens=2000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Error fixing inconsistencies: {e}")
            return story_content
    
    def validate_character_consistency(self, character: Dict, actions: List[str]) -> List[str]:
        """Validate if character actions are consistent with their profile"""
        # Implementation for character action validation
        pass