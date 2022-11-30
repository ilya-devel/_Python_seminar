class Polynomial:
    def __init__(self, fm):
        self.poly = fm

    def __call__(self, *args, **kwargs):
        tmp = [self.poly[0]]
        for i in range(1, len(self.poly)):
            tmp.append(self.poly[i] * args[0] ** i)
        return sum(tmp)

    def __add__(self, other):
        return Polynomial(list(map(lambda x: x[0] + x[1], zip(self.poly, other.poly))))


poly = Polynomial([10, -1])
print(poly(0))  # 10
print(poly(1))  # 9
print(poly(2))  # 8

print()

poly1 = Polynomial([0, 0, 1])
print(poly1(-2))  # 4
print(poly1(-1))  # 1
print(poly1(0))  # 0
print(poly1(1))  # 1
print(poly1(2))  # 4
print()
poly2 = Polynomial([0, 0, 2])
print(poly2(-2))
print(poly2(-1))
print(poly2(0))
print(poly2(1))
print(poly2(2))
print()
poly3 = poly1 + poly2
print(poly3(-2))
print(poly3(-1))
print(poly3(0))
print(poly3(1))
print(poly3(2))
print()
