from .prompt import Prompt


class RegexPrompt(Prompt):
    """
    Expects a regex pattern matching a provided string.

    Example:
        Question: Write a regex pattern which matches '40-90'
        Answer: '^[0-9]{2}-[0-9]{2}$'
    """
    def __init__(self):
        super().__init__()
        self.string: str = ''
        self.pattern: str = None
    
    @property
    def question(self):
        return f'Write a regex pattern which matches the string: {self.string}'
    