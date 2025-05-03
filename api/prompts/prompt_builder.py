import random
from . import Prompt
from components import Quantifier, CharClass, Group, Anchor, Literal


MIN_DIFFICULTY = 0
MAX_DIFFICULTY = 4

CREDIT_MULTIPLIER = 2.25  
BASE_CREDITS = 4  # number of credits for minimum difficulty

COMPONENTS = [Literal, CharClass, Group]

SEPARATORS = [' ', '-', '_', ':', ',']
CHANCE_OF_SEPARATOR = 0.5

CHANCE_OF_QUANTIFIER = 0.4


def add_component(prompt) -> int:
    """
    Add a random component to the prompt.

    :param prompt: The Prompt object to add components to.
    :return: The number of credits used.
    """
    component = random.choice(COMPONENTS)
    price = component.PRICE

    prompt.add_component(component.random()) 
    
    if component.QUANTIFIER_POSSIBLE and random.random() < CHANCE_OF_QUANTIFIER:
        prompt.add_component(Quantifier.random())
        price += Quantifier.PRICE

    return price 


def build_prompt(difficulty=0, num_strings=3) -> Prompt:
    """
    Build a regex prompt with random components.

    :param difficulty: The difficulty level of the prompt (0-4).
    :param num_strings: The number of strings to generate.
    :return: A Prompt object containing the regex pattern and generated strings.
    """
    prompt = Prompt(difficulty)
    prompt.add_component(Anchor('^'))

    # calculate credits based on difficulty
    credit = round(difficulty * CREDIT_MULTIPLIER) + BASE_CREDITS 

    # add components until credits are exhausted
    while credit > 0:
        credit -= add_component(prompt)

        # randomly add a literal separater for clarity
        if random.random() < CHANCE_OF_SEPARATOR:
            sep = random.choice(SEPARATORS)
            prompt.add_component(Literal(sep))

    # build and return prompt
    prompt.add_component(Anchor('$'))
    prompt.build(num_strings)
    return prompt


def main():
    for i in range(5):
        prompt = build_prompt(i, 3)
        print(prompt)


if __name__ == '__main__':
    main()
