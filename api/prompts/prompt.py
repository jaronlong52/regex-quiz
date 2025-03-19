class Prompt:
    def __init__(self):
        self.example: str = None
   
    def __str__(self):
        return f'{self.__class__.__name__}: {self.question} | Example: {self.example}'

    @property
    def question(self):
        return ''
