from . import Prompt
from components import Quantifier, CharClass, Anchor, Group


MIN_DIFFICULTY = 0
MAX_DIFFICULTY = 4


def build_prompt(difficulty=0, num_strings=3) -> Prompt:
    """
    Build a regex prompt with random components.

    :param difficulty: The difficulty level of the prompt (0-4).
    :param num_strings: The number of strings to generate.
    :return: A Prompt object containing the regex pattern and generated strings.
    """
    prompt = Prompt()

    prompt.add_component(Anchor('^'))
    prompt.add_component(CharClass.random())
    prompt.add_component(Group.random())
    prompt.add_component(Quantifier.random())
    prompt.add_component(CharClass.random())
    prompt.add_component(Anchor('$'))

    prompt.build(num_strings)
    return prompt


def main():
    prompt = build_prompt()
    print(prompt)


if __name__ == '__main__':
    main()
