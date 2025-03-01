class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, num):
        self.value += num

    def get_value(self):
        return self.value

calc = Calculator(10)
calc.add(5)
print(calc.get_value())