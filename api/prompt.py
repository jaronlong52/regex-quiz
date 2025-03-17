class Prompt:
    def __init__(self):
        self.example: str = None
   
    def __str__(self):
        return f'{self.__class__.__name__}: {self.question} | Example: {self.example}'

    @property
    def question(self):
        return ''


class RegexPrompt(Prompt):
    """
    Expects a regex pattern matching a provide string.

    Example:
        Prompt: Write a regex pattern which matches '40-90'
        Answer: '^[0-9]{2}-[0-9]{2}$'
    """
    def __init__(self):
        super().__init__()
        self.string: str = ''
        self.pattern: str = None
    
    @property
    def question(self):
        return f'Write a regex pattern which matches the string: {self.string}'
    

class MatchPrompt(Prompt):
    """
    Expects a matching string for the provided regex pattern.
    
    Example:
        Prompt: Write a string which matches ^[a-z]{3}$
        Answer: 'abc'
    """
    def __init__(self):
        super().__init__()
        self.string: str = ''
        self.pattern: str = None
    
    def question(self) -> str:
        return f'Write a string which matches the pattern: {self.pattern}'
    