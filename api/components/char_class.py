import re
import string
import random
from .component import Component


class CharClass(Component):
    def __init__(self, pattern: str):
        """
        Represents a regex character class.
        """
        super().__init__()

        assert isinstance(pattern, str), "CharClass string must be a string"
        self.pattern = pattern

        # validate regex pattern
        try:
            re.compile(self.pattern)
        except re.error:
            raise ValueError(f"Invalid regex character class: {self.pattern}")

        # extract valid characters
        self.characters = self._expand_char_class()
        if not self.characters:
            raise ValueError(f"Character class {self.pattern} does not match any characters.")

    def _expand_char_class(self):
        """Extracts characters that belong to the given regex character class."""
        predefined_classes = {
            "\\d": string.digits,
            "\\w": string.ascii_letters + string.digits + "_",
            "\\s": " \t\n",
            ".": string.printable,
        }

        if self.pattern in predefined_classes:
            return list(predefined_classes[self.pattern])

        # extract characters manually for complex classes
        pattern = re.compile(self.pattern)
        return [char for char in string.printable if pattern.fullmatch(char)]

    def get_sample(self) -> str:
        """Returns a random character that belongs to the character class."""
        if not self.characters:
            raise ValueError(f"Cannot generate sample: No characters match {self.pattern}.")
        return random.choice(self.characters)
    
    @staticmethod
    def _generate_random(min_chars=2, max_chars=5) -> str:
        """
        Generates a regex character class containing a random subset of letters.
        
        :param min_chars: Minimum number of characters to include.
        :param max_chars: Maximum number of characters to include.
        :return: A regex character class string (e.g., "[abc]").
        """
        num_chars = random.randint(min_chars, max_chars)
        # Choose a random sample from letters (you can extend to digits or other characters if needed)
        selected_chars = random.sample(string.ascii_letters, num_chars)
        return "[" + "".join(selected_chars) + "]"
    
    @staticmethod
    def random() -> 'CharClass':
        """
        Returns a random valid CharClass.
        """
        random_classes = [
            r"\d",  # Digit class
            r"\w",  # Word character class
            r"\s",  # Whitespace class
            r"[a-zA-Z]",  # Letter class (lowercase + uppercase)
            r"[a-z]",  # Lowercase letters
            r"[A-Z]",  # Uppercase letters
            r"[0-9]",  # Digits
            CharClass._generate_random(),  # Random character class, e.g., "[abc]"
            CharClass._generate_random(),
        ]
        random_choice = random.choice(random_classes)
        return CharClass(random_choice)


def main():
    """Runs basic test cases for the CharClass."""
    char_class1 = CharClass("[a-zA-Z]")
    print(char_class1)  # character Class: [a-zA-Z]
    print(char_class1.get_sample())  # random letter

    digit_class = CharClass("\\d")
    print(digit_class)  # character Class: \d
    print(digit_class.get_sample())  # random digit

    whitespace_class = CharClass("\\s")
    print(whitespace_class)  # character Class: \s
    print(repr(whitespace_class.get_sample()))  # random whitespace (e.g., '\t', '\n', ' ')

    dot_class = CharClass(".")
    print(dot_class)  # character Class: .
    print(repr(dot_class.get_sample()))  # random printable character


if __name__ == "__main__":
    main()
