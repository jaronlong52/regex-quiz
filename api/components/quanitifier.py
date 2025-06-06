import random
from .component import Component


class Quantifier(Component):
    """
    Represents a regex quantifier, which specifies how many times a pattern can occur.
    """

    PRICE = 2
    QUANTIFIER_POSSIBLE = False

    MAX_ADDER = 3

    def __init__(self, value: tuple | int):
        """
        Initializes a Quantifier object with a given value.
        :param value: An integer or a tuple of integers representing the quantifier range.
        """
        super().__init__()

        if isinstance(value, int):  
            self.value = (value, value)
        elif isinstance(value, tuple) and len(value) in {1, 2}:
            self.value = value
        else:
            raise ValueError('Quantifier must be an int or a tuple of length 1 or 2')

        first = self.value[0]
        assert isinstance(first, int), 'First quantifier value must be an integer'
        second = self.value[1]
        assert second is None or isinstance(second, int), 'Second quantifier value must be None or an integer'

        if second is not None and first > second:
            second, first = first, second
            self.value = (first, second)

        self.pattern = self._generate_string(first, second)

    def _generate_string(self, first: int, second: int) -> str:
        """Generates the appropriate regex quantifier string."""
        if second is None:  # zero/one or more
            return (
                f'{{{first}}}' if first != 0 else '*'
            ) if first > 1 else ('+' if first == 1 else '*')

        if first == second:  # exact
            return f'{{{first}}}'

        if first == 0 and second == 1:  # optional
            return '?'

        if first == 0 and second is None:  # zero or more
            return '*'

        if first == 1 and second is None:  # one or more
            return '+'

        return f'{{{first},{second}}}' if second is not None else f'{{{first},}}'

    def get_quantity(self) -> int:
        """Returns a random number within the quantifier range."""
        # if the upper bound is None, set a default maximum for random generation.
        if self.value[1] is None:
            default_max = self.value[0] + Quantifier.MAX_ADDER
            return random.randint(self.value[0], default_max)
        elif self.value[0] == self.value[1]:
            return self.value[0]
        else:
            return random.randint(self.value[0], self.value[1])
  

    @staticmethod
    def random() -> 'Quantifier':
        """Returns a random valid quantifier."""
        options = [
            (random.randint(0, 4), random.randint(0, 4)),
            (random.randint(0, 2), None),
            (0, 1),
            (1, None),
            (0, None)
        ]
        return Quantifier(random.choice(options))


def main():
    """Runs basic test cases for the Quantifier."""
    test_cases = [
        (1, "{1}"),
        ((5, 5), "{5}"),
        ((1, 2), "{1,2}"),
        ((7, 20), "{7,20}"),
        ((0, 1), "?"),
        ((0, None), "*"),
        ((1, None), "+"),
    ]

    for value, expected in test_cases:
        quantifier = Quantifier(value)
        print(f'Quantifier({value}) -> {quantifier}')
        assert str(quantifier) == expected, f'Failed for {value}, got {quantifier}'

    for _ in range(5):
        rand_quant = Quantifier.random()
        print(f"Random Quantifier: {rand_quant}")


if __name__ == '__main__':
    main()
