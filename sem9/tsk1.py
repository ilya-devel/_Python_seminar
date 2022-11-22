class LittleBell:
    def sound(self):
        print('ding')


bell = LittleBell()
for _ in range(3):
    bell.sound()
print()
for _ in range(3):
    LittleBell().sound()
