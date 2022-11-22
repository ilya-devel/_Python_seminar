class MinMaxWordFinder:
    def __init__(self):
        self.lst_word = []

    def add_sentence(self, row: str):
        self.lst_word += row.split()

    def shortest_word(self):
        min_len = sorted([len(x) for x in self.lst_word])[0]
        return sorted(list(filter(lambda x: len(x) == min_len, self.lst_word)))

    def longest_word(self):
        max_len = sorted([len(x) for x in self.lst_word])[-1]
        return sorted(set(filter(lambda x: len(x) == max_len, self.lst_word)))


stack = MinMaxWordFinder()
stack.add_sentence('abc def longest')
stack.add_sentence('ad it alkjdfadgag it')
stack.add_sentence('zjdfl;kjadlkjfl;dajkj zjdfl;kjadlkjfl;dajkj ajdfl;kjadlkjfl;dajkj')
print(stack.shortest_word())
print(stack.longest_word())