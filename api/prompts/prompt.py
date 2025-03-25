from ..components import Quantifier

class Prompt:
    def __init__(self):
        self.string: str = ''
        self.pattern: str = ''
   
    def __str__(self):
        return f'{self.__class__.__name__}: {self.question} | Example: {self.example}'

    @property
    def question(self):
        return ''
    
    def add_quantifier(self, quantifier: Quantifier):
        self.pattern += quantifier.string
