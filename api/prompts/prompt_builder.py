import random
from . import Prompt
from components import Quantifier, CharClass, Group, Anchor, Literal


MIN_DIFFICULTY = 0
MAX_DIFFICULTY = 4

# (Component, credit, add_quanitifier)
COMPONENT_DICTIONARY = [
    (Literal, 3, False),
    (CharClass, 3, True),
    (Group, 4, True)
]


def add_component(prompt) -> int:
    """
    Add a random component to the prompt.

    :param prompt: The Prompt object to add components to.
    :return: The number of credits used.
    """
    selection = random.choice(COMPONENT_DICTIONARY)
    component = selection[0].random()
    credit = selection[1]
    add_quanitifier = selection[2]

    prompt.add_component(component)
    
    if add_quanitifier and random.randint(0, 1):
        prompt.add_component(Quantifier.random())
        credit += 2

    return credit


def build_prompt(difficulty=0, num_strings=3) -> Prompt:
    """
    Build a regex prompt with random components.

    :param difficulty: The difficulty level of the prompt (0-4).
    :param num_strings: The number of strings to generate.
    :return: A Prompt object containing the regex pattern and generated strings.
    """
    prompt = Prompt(difficulty)
    prompt.add_component(Anchor('^'))

    credit = ((difficulty + 1) * 4) + 1 

    while credit > 0:
        credit -= add_component(prompt)

    prompt.add_component(Anchor('$'))

    prompt.build(num_strings)
    return prompt


def main():
    for i in range(5):
        prompt = build_prompt(i, 3)
        print(prompt)


if __name__ == '__main__':
    main()
