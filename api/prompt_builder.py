from .prompts import RegexPrompt


def build_regex() -> RegexPrompt:
    new_prompt = RegexPrompt()

    print(new_prompt.question)
    return new_prompt


def main():
    prompt = build_regex()


if __name__ == '__main__':
    main()
