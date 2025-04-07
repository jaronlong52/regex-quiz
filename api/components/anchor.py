from .component import Component

class Anchor(Component):
    def __init__(self, pattern: str):
        """
        Represents a regex anchor.
        """
        super().__init__()

        assert isinstance(pattern, str), "Anchor string must be a string"
        if not self._is_valid_anchor(pattern):
            raise ValueError(f"Invalid regex anchor: {pattern}")

        self.pattern = pattern
    
    def __str__(self) -> str:
        return self.pattern
    
    def _is_valid_anchor(self, pattern: str) -> bool:
        """Check if the given anchor is valid."""
        return pattern in ['^', '$']
    