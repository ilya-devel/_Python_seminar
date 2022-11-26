class __Values:
    def __init__(self):
        self.lst_val = []

    def add_number(self, values):
        self.lst_val.append(values)


class MinStat(__Values):
    def result(self):
        return min(self.lst_val) if self.lst_val else None


class MaxStat(__Values):
    def result(self):
        return max(self.lst_val) if self.lst_val else None

class AverageStat(__Values):
    def result(self):
        return sum(self.lst_val)/len(self.lst_val) if self.lst_val else None

# Пример 1.
values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

# Пример 2.
mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())

# Пример 3.
values = [1, 0, 0]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))