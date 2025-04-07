import random
from .component import Component


DICTIONARY = [ 
    'dog', 'cat', 'blue', 'red', 'six', 'mom', 'dad', 'sun', 'sky', 'fun',
    'zip', 'toy', 'box', 'cup', 'pen', 'lip', 'car', 'run', 'hop', 'win',
    'tree', 'rock', 'bird', 'fish', 'ship', 'lake', 'sand', 'rain', 'wind', 'fire',
    'ab', 'xy', 'ce', 'aeiou', 'xyz', 'abc', 'def', 'ghi', 'jkl', 'mno',
]


class Group(Component):
    def __init__(self, pattern: str):
        """
        Represents a regex group.
        """
        super().__init__()

        assert isinstance(pattern, str), "Group pattern must be a string"

        self.pattern = pattern
        self.subpatterns = self._extract_subpatterns(pattern)

    def __str__(self) -> str:
        return f"({self.pattern})"
    
    def get_sample(self) -> str:
        return random.choice(self.subpatterns)
    
    def _extract_subpatterns(self, pattern: str) -> list[str]:
        """Extracts subpatterns from a regex group."""
        return pattern.split('|')
    
    @staticmethod
    def random(min_patterns=1, max_patterns=2) -> 'Group':
        """Generates a regex Group containing a random subset of patterns."""
        num_patterns = random.randint(min_patterns, max_patterns)
        patterns = [Group._random_word() for _ in range(num_patterns)]
        return Group("|".join(str(pattern) for pattern in patterns))
    
    @staticmethod
    def _random_word() -> str:
        """Generates a random word of a given length."""
        return random.choice(DICTIONARY)
