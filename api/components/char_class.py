import re
import string
import random


class CharClass:
    def __init__(self, value: str):
        """
        Represents a regex character class.
        """
        assert isinstance(value, str), "CharClass value must be a string"
        self.value = value

        # validate regex pattern
        try:
            re.compile(self.value)
        except re.error:
            raise ValueError(f"Invalid regex character class: {self.value}")

        # extract valid characters
        self.characters = self._expand_char_class()
        if not self.characters:
            raise ValueError(f"Character class {self.value} does not match any characters.")

    def _expand_char_class(self):
        """Extracts characters that belong to the given regex character class."""
        predefined_classes = {
            "\\d": string.digits,
            "\\w": string.ascii_letters + string.digits + "_",
            "\\s": " \t\n",
            ".": string.printable,
        }

        if self.value in predefined_classes:
            return list(predefined_classes[self.value])

        # extract characters manually for complex classes
        pattern = re.compile(self.value)
        return [char for char in string.printable if pattern.fullmatch(char)]

    def __str__(self):
        return f"Character Class: {self.value}"

    def get_sample(self) -> str:
        """Returns a random character that belongs to the character class."""
        if not self.characters:
            raise ValueError(f"Cannot generate sample: No characters match {self.value}.")
        return random.choice(self.characters)
    
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
            r"[^\w\s]",  # Non-alphanumeric class
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
