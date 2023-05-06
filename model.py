class Model:
    def __init__(self) -> None:

        self.previous_value: str = ''
        self.value: str = ''
        self.operator: str = ''

    def calculate(self, caption) -> str:
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
        
        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value

        elif caption == '%':
            pass

        elif caption == '.':
            if not caption in self.value:
                self.value += caption

        elif isinstance(caption, int):
            self.value += str(caption)

        else:
            self.operator = caption

        return self.value
