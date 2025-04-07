import random
from . import Prompt
from components import Component, Quantifier, CharClass, Group, Anchor


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

    credit = (difficulty + 1) * 4 

    while credit > 0:
        credit -= add_component(prompt)

    prompt.add_component(Anchor('$'))

    prompt.build(num_strings)
    return prompt


def add_component(prompt) -> int:
    """
    Add a random component to the prompt.

    :param prompt: The Prompt object to add components to.
    :return: The number of credits used.
    """
    component: tuple[Component, int] = random.choice([
        (CharClass, 3),
        (Group, 4)
    ])
    prompt.add_component(component[0].random())
    credit = component[1]
    
    if random.randint(0, 1):
        prompt.add_component(Quantifier.random())
        credit += 2

    return credit


def main():
    prompt = build_prompt(4)
    print(prompt)


if __name__ == '__main__':
    main()
