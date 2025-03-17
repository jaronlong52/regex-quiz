class Quantifier():
    def __init__(self, value: tuple):
        if not isinstance(value, tuple):  
            self.value = (value, )
        else: 
            self.value = value

        assert len(self.value) == 1 or len(self.value) == 2, 'Quantifier must have 1 or 2 values'

        self.string = ''
        first = self.value[0]
        assert first is not None and isinstance(first, int), 'First quantifier value must be int'

        # exact value
        if len(self.value) == 1:
            self.string = f'{{{first}}}'
            return

        second = self.value[1]
        assert second is None or isinstance(second, int), 'Second quantifier value must be None or an int'

        # shorthand cases
        if first == 0 and second is None:
            self.string = '*'
            return
        if first == 1 and second is None:
            self.string = '+'
            return
        if first == 0 and second == 1:
            self.string = '?'
            return

        # range 
        self.string = f'{{{first},{second or ''}}}'
    
    def __str__(self):
        return self.string


def main():
    print(Quantifier(1))
    print(Quantifier((1,2)))
    print(Quantifier(0))
    print(Quantifier((0,1)))
    print(Quantifier((0,None)))
    print(Quantifier((1,None)))


if __name__ == '__main__':
    main()
