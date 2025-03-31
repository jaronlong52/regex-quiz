from . import MatchPrompt, RegexPrompt
from components import Quantifier, CharClass


DIFFICULTY = [0, 5]


def build_regex() -> RegexPrompt:
    new_prompt = RegexPrompt()
    new_prompt.add_component(CharClass.random())
    new_prompt.add_component(Quantifier.random())
    new_prompt.add_component(CharClass.random())
    new_prompt.add_component(Quantifier.random())
    new_prompt.build()
    return new_prompt


def build_match() -> MatchPrompt:
    new_prompt = MatchPrompt()
    new_prompt.add_component(CharClass.random())
    new_prompt.add_component(Quantifier.random())
    new_prompt.add_component(CharClass.random())
    new_prompt.add_component(Quantifier.random())
    new_prompt.build()
    return new_prompt


def main():
    prompt = build_regex()
    print(prompt)
    prompt = build_match()
    print(prompt)


if __name__ == '__main__':
    main()
