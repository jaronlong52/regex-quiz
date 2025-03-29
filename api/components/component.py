class Component:
    def __init__(self):
        """
        Represents a regex component, such as a character class or quantifier.
        """
        self.pattern: str = ''
    
    def __str__(self):
        return self.pattern
