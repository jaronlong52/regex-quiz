import re
from ..components import Component, CharClass, Quantifier


class Prompt:
    def __init__(self):
        self.components: list[Component] = []
        self.string: str = ''
        self.pattern: str = ''
   
    def __str__(self):
        return f'{self.__class__.__name__}: {self.question} | Pattern: {self.pattern} | String: {self.string}'
    
    @property
    def question(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def to_dict(self) -> dict:
        return {
            'type': self.__class__.__name__,
            'question': self.question,
            'pattern': self.pattern,
            'string': self.string
        }
    
    def add_component(self, component: Component):
        self.components.append(component)
    
    def build(self):
        """
        Build the regex pattern by combining all components.
        """
        for component in self.components:
            self.pattern += str(component) 

            if isinstance(component, CharClass):
                self.string += component.get_sample()
            elif isinstance(component, Quantifier):
                quantity = component.get_quantity()
                if self.string:
                    self.string += self.string[-1] * (quantity - 1)
                else:
                    raise ValueError("Quantifier encountered without a preceding sample character.")
        
        # validate the final regex pattern
        try:
            re.compile(self.pattern)
        except re.error as e:
            raise ValueError(f"The generated regex pattern is invalid: {self.pattern}. Error: {e}")
