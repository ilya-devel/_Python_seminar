class Button:
    def __init__(self, name='btn'):
        self.name = name
        self.click_btn_count = 0

    def click(self):
        self.click_btn_count += 1

    def click_count(self):
        return self.click_btn_count

    def reset(self):
        self.click_btn_count = 0


a = Button()
a.click()
a.click()
print(a.click_count())
a.click()
print(a.click_count())
a.reset()
print(a.click_count())