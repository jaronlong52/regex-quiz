from . import Prompt
from components import Quantifier, CharClass


MIN_DIFFICULTY = 0
MAX_DIFFICULTY = 4


def build_prompt(num_strings: int =3) -> Prompt:
    """
    Build a regex prompt with random components.
    """
    prompt = Prompt()
    prompt.add_component(CharClass.random())
    prompt.add_component(Quantifier.random())
    prompt.add_component(CharClass.random())
    prompt.add_component(Quantifier.random())
    prompt.build(num_strings)
    return prompt


def main():
    prompt = build_prompt()
    print(prompt)


if __name__ == '__main__':
    main()
