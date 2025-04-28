import re
from components import Component, CharClass, Quantifier, Anchor, Group, Literal


class Prompt:
    def __init__(self, difficulty: int = 0):
        self.components: list[Component] = []
        self.difficulty = difficulty
        self.pattern: str = ''
        self.strings: list[str] = None
    
    def __str__(self) -> str:
        return f"Prompt(difficutly={self.difficulty}, pattern={self.pattern}, strings={self.strings})"
   
    def to_dict(self) -> dict:
        return {
            'difficulty': self.difficulty,
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
        strings = []

        for _ in range(num_strings * 10):
            strings.append(self.generate_sample())
        
        strings = set(strings)  # remove duplicates
        strings = list(strings)[:num_strings]  # limit to num_strings

        self.strings = strings
    
    def generate_sample(self) -> str:
        """
        Generates a sample from the regex pattern.
        """  
        sample = ''
        index = 0

        while index < len(self.components):
            component = self.components[index]
            next_ = self.components[index + 1] if index + 1 < len(self.components) else None

            match component:
                case Anchor():
                    index += 1
                case CharClass() as cc:
                    if isinstance(next_, Quantifier):
                        for _ in range(next_.get_quantity()):
                            sample += cc.get_sample()
                        index += 2
                    else:
                        sample += cc.get_sample()
                        index += 1
                case Literal() as lit:
                    sample += lit.get_sample()
                    index += 1
                case Group() as grp:
                    if isinstance(next_, Quantifier):
                        sample += grp.get_sample() * next_.get_quantity()
                        index += 2
                    else:
                        sample += grp.get_sample()
                        index += 1
                case _:
                    raise ValueError(f"Unhandled component type: {component}")
        
        return sample
        
