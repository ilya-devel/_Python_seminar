class Balance:
    def __init__(self):
        self.right_cup = []
        self.left_cup = []

    def add_right(self, value:int):
        self.right_cup.append(value)

    def add_left(self, value:int):
        self.left_cup.append(value)

    def result(self):
        if sum(self.right_cup) > sum(self.left_cup):
            return 'R'
        elif sum(self.right_cup) < sum(self.left_cup):
            return 'L'
        else:
            return '='


# scale = Balance()
# scale.add_left(11)
# scale.add_right(7)
# print(scale.result())
# scale.add_left(7)
# scale.add_right(11)
# print(scale.result())
# scale.add_left(7)
# scale.add_right(17)
# print(scale.result())

balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
print(balance.result())
balance.add_left(1)
print(balance.result())