class SeaMap:
    def __init__(self):
        self.field = [['.' for _ in range(10)] for _ in range(10)]
        pass

    def shoot(self, row, col, result):
        if result == 'miss':
            self.field[row][col] = '*'
        elif result == 'hit':
            self.field[row][col] = 'x'
        elif result == 'sink':
            self.field[row][col] = 'x'
            for irow in [-1, 0, 1]:
                for icol in [-1, 0, 1]:
                    if (0 <= (row + irow) <= 9 and 0 <= (col + icol) <= 9):
                        if irow == 0 and icol == 0:
                            pass
                        else:
                            self.field[row + irow][col + icol] = '*'

    def cell(self, row, col):
        return self.field[row][col]

if __name__ == '__main__':
    sm = SeaMap()
    sm.shoot(2, 0, 'miss')
    sm.shoot(6, 9, 'miss')
    for row in range(10):
        for col in range(10):
            print(sm.cell(row, col), end='')
        print()
    print()
    sm = SeaMap()
    sm.shoot(2, 0, 'sink')
    sm.shoot(6, 9, 'hit')
    for row in range(10):
        for col in range(10):
            print(sm.cell(row, col), end='')
        print()
    print()
    sm = SeaMap()
    sm.shoot(0, 0, 'sink')
    sm.shoot(0, 9, 'sink')
    sm.shoot(9, 0, 'sink')
    sm.shoot(9, 9, 'sink')
    for row in range(10):
        for col in range(10):
            print(sm.cell(row, col), end='')
        print()
    print()