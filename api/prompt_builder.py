from .prompts import RegexPrompt
from .components import Quantifier, CharClass


def build_regex() -> RegexPrompt:
    new_prompt = RegexPrompt()
    new_prompt.add_component(CharClass.random())
    new_prompt.add_component(Quantifier.random())
    new_prompt.add_component(CharClass.random())
    new_prompt.add_component(Quantifier.random())
    new_prompt.build()
    return new_prompt


def main():
    prompt = build_regex()
    print(prompt)


if __name__ == '__main__':
    main()
