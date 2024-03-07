class Button:
    def __init__(self):
        self.click_cnt = 0

    def click(self):
        self.click_cnt += 1
        
    def click_count(self):
        return self.click_cnt
        
    def reset(self):
        self.click_cnt = 0

button = Button()
button.click()
button.click()
print(button.click_count())
button.reset()
print(button.click_count())