class OddEvenSeparator:
    def __init__(self):
        self.lst_odd = []
        self.lst_even = []

    def add_number(self, value: int):
        if value % 2 == 0:
            self.lst_even.append(value)
        else:
            self.lst_odd.append(value)

    def odd(self):
        return ', '.join(map(str, self.lst_odd))

    def even(self):
        return ', '.join(map(str, self.lst_even))


stack = OddEvenSeparator()
stack.add_number(11)
stack.add_number(4)
stack.add_number(6)
stack.add_number(7)
stack.add_number(2)
print(stack.odd())
print(stack.even())
