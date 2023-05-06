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

        elif caption == '<':
            self.value = self.value[:len(self.value)-1]

        elif caption == '.':
            if not caption in self.value:
                self.value += caption

        elif caption == '=':
            self.value = str(self._evaluate())

        elif isinstance(caption, int):
            self.value += str(caption)

        else:
            if self.value:
                
                self.operator = caption
                self.previous_value = self.value
                self.value = ''

        return self.value


    def _evaluate(self):
        return eval(self.previous_value + self.operator + self.value)