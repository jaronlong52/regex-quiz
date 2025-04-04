import re
from components import Component, CharClass, Quantifier


class Prompt:
    def __init__(self):
        self.components: list[Component] = []
        self.pattern: str = ''
        self.strings: list[str] = None
    
    def __str__(self) -> str:
        return f"Prompt(pattern={self.pattern}, strings={self.strings})"
   
    def to_dict(self) -> dict:
        return {
            'pattern': self.pattern,
            'strings': self.strings
        }
    
    def add_component(self, component: Component):
        self.components.append(component)
    
    def build(self, num_strings: int = 1):
        """
        Build the regex pattern by combining all components.
        """
        # build the regex pattern from components
        for component in self.components:
            self.pattern += str(component) 
        
        # validate the regex pattern
        try:
            re.compile(self.pattern)
        except re.error as e:
            raise ValueError(f"The generated regex pattern is invalid: {self.pattern}. Error: {e}")

        # generate sample strings based on the regex pattern
        self.strings = []

        for _ in range(num_strings):
            self.strings.append(self.generate_sample())
    
    def generate_sample(self) -> str:
        """
        Generates a sample from the regex pattern.
        """  
        sample = ''
        index = 0

        while index < len(self.components):
            component = self.components[index]
            next_ = self.components[index + 1] if index + 1 < len(self.components) else None

            if isinstance(component, CharClass):
                if isinstance(next_, Quantifier):
                    sample += component.get_sample() * next_.get_quantity()
                    index += 2
                else:
                    sample += component.get_sample()
                    index += 1
        
        return sample
        
