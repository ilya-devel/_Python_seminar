class BigBell:
    def __init__(self):
        self.uta = True

    def sound(self):
        if self.uta:
            print('ding')
            self.uta = False
        else:
            print('dong')
            self.uta = True


bell = BigBell()
for _ in range(3):
    bell.sound()