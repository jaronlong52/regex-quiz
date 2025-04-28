class Component:
    """
    Represents a regex component, such as a character class or quantifier.
    """

    PRICE = 0
    QUANTIFIER_POSSIBLE = False

    def __init__(self, pattern: str = ''):
        """
        Initializes a regex component with a given pattern.

        :param pattern: The regex pattern for this component.
        """
        self.pattern = pattern
    
    def __str__(self):
        return self.pattern
    
    def get_sample(self) -> str:
        raise NotImplementedError("Subclasses must implement this method.")
    
    @staticmethod
    def random(self) -> 'Component':
        raise NotImplementedError("Subclasses must implement this method.")
