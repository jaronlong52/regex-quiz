import random
from .component import Component

DICTIONARY = [ 
    'tower', 'batch', 'small', 'large', 'even', 'odd', 'two', 'ten', 'red', 'green',
    'lock', 'key', 'door', 'car', 'base', 'mount', 'level', 'half', 'hope', 'wish', 
]

class Literal(Component):
    """
    Represents a literal regex pattern.
    """

    PRICE = 3
    QUANTIFIER_POSSIBLE = False

    def __init__(self, pattern: str):
        """
        Initializes a Literal object with a given pattern.
        """
        assert isinstance(pattern, str), "Literal pattern must be a string"
        super().__init__(pattern)
    
    def get_sample(self) -> str:
        return self.pattern
    
    @staticmethod
    def random() -> 'Literal':
        """Generates a Literal containing a random value from the dictionary."""
        return Literal(random.choice(DICTIONARY))
    