from .prompt import Prompt


class MatchPrompt(Prompt):
    """
    Expects a matching string for the provided regex pattern.
    
    Example:
        Question: Write a string which matches ^[a-z]{3}$
        Answer: 'abc'
    """
    def __init__(self):
        super().__init__()
    
    @property
    def question(self) -> str:
        return f'Write a string which matches the pattern: {self.pattern}'
    