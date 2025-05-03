import random
from .component import Component

class Anchor(Component):
    """
    Represents a regex anchor, which matches the start or end of a string.
    """

    PRICE = 0
    QUANTIFIER_POSSIBLE = False

    def __init__(self, pattern: str):
        """
        Initializes an Anchor object with a given pattern.
        """
        super().__init__(pattern)

        assert isinstance(pattern, str), "Anchor string must be a string"
        if not self._is_valid_anchor(pattern):
            raise ValueError(f"Invalid regex anchor: {pattern}")
    
    def get_sample(self) -> str:
        return ''
    
    def _is_valid_anchor(self, pattern: str) -> bool:
        """Check if the given anchor is valid."""
        return pattern in ['^', '$']
    
    @staticmethod
    def random() -> 'Anchor':
        """Generates a random Anchor."""
        return Anchor('^' if random.choice([True, False]) else '$')
    