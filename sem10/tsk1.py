class Selector:
    def __init__(self, lst):
        self.lst = lst

    def get_odds(self):
        return [x for x in self.lst if x % 2 != 0]

    def get_evens(self):
        return [x for x in self.lst if x % 2 == 0]


values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))

print()

values = [6, 6, 0, 4, 8, 7, 6, 4, 7, 5]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))
