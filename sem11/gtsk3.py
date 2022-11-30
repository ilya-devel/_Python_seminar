class Date:
    day_in_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        self_days = sum([Date.day_in_months[x] for x in Date.day_in_months.keys() if x < self.month]) + self.day
        other_days = sum([Date.day_in_months[x] for x in Date.day_in_months.keys() if x < other.month]) + other.day
        return self_days - other_days


jan5 = Date(1, 5)
jan1 = Date(1, 1)
print(jan5 - jan1)
print(jan1 - jan5)
print(jan1 - jan1)
print(jan5 - jan5)

print()

mar1 = Date(3, 1)
jan1 = Date(1, 1)
print(mar1 - jan1)
print(jan1 - mar1)
print(jan1 - jan1)
print(mar1 - mar1)
