class ReversedList:
    def __init__(self, lst):
        self.lst = lst[::-1]

    def __iter__(self):
        return self.lst

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, item):
        return self.lst[item]


rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])

print()

rl = ReversedList([])
print(len(rl))

print()

rl = ReversedList([10])
print(len(rl))
print(rl[0])