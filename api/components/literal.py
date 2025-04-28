import random
from .component import Component

DICTIONARY = [ 
    'tower', 'batch', 'small', 'large', 'even', 'odd', 'two', 'ten', 'red', 'green',
    'lock', 'key', 'door', 'car', 'base', 'mount', 'level', 'half', 'hope', 'wish', 
]

class Literal(Component):
    def __init__(self, pattern: str):
        """
        Represents a literal regex pattern.
        """
        super().__init__()

        self.pattern = pattern
    
    def __str__(self) -> str:
        return self.pattern
    
    def get_sample(self) -> str:
        return self.pattern
    
    @staticmethod
    def random() -> 'Literal':
        """Generates a Literal containing a random value from the dictionary."""
        return Literal(random.choice(DICTIONARY))
    

def main():
    """Runs basic test cases for the Literal."""
    pass


if __name__ == '__main__':
    main()