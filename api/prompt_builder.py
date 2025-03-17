from api.prompt import RegexPrompt


def build_regex() -> RegexPrompt:
    new_prompt = RegexPrompt()
    new_prompt.string = '40-90'
    new_prompt.pattern = '^[0-9]{2}-[0-9]{2}$'

    print(new_prompt.question)
    return new_prompt


def main():
    prompt = build_regex()


if __name__ == '__main__':
    main()
