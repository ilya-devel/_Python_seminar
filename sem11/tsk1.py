class Car:
    def __init__(self, color, year, max_speed):
        self.color = color
        self.year = year
        self.max_speed = max_speed

    def __add__(self, other):
        return self.max_speed + other.max_speed

    def __iadd__(self, other):
        return self.max_speed + other

    def __radd__(self, other):
        return self.max_speed + other


bmw = Car('black', 2018, 250)
audi = Car('yellow', 2016, 240)
moskvich = Car('green', 1986, 500)

# print((bmw + audi + moskvich).year)
print(bmw+audi+moskvich)
print(100 + bmw)
