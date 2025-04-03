import re
from components import Component, CharClass, Quantifier


class Prompt:
    def __init__(self):
        self.components: list[Component] = []
        self.pattern: str = ''
        self.strings: list[str] = None
   
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
            string = ''

            for component in self.components:
                if isinstance(component, CharClass):
                    string += component.get_sample()
                elif isinstance(component, Quantifier):
                    quantity = component.get_quantity()
                    if string:
                        string += string[-1] * (quantity - 1)
                    else:
                        raise ValueError("Quantifier encountered without a preceding sample character.")
                
            self.strings.append(string)
