class LeftParagraph:
    def __init__(self, num):
        self.num = num
        self.word_list = [""]

    def add_word(self, text):
        if len(self.word_list[-1]) + len(text) + 1 > self.num:
            self.word_list.append(text)
        else:
            if len(self.word_list[-1]) == 0:
                self.word_list[-1] += text
            else:
                self.word_list[-1] = self.word_list[-1] + " " + text

    def end(self):
        for i in self.word_list:
            print(i)

class RightParagraph:
    def __init__(self, num):
        self.num = num
        self.word_list = [""]

    def add_word(self, text):
        if len(self.word_list[-1]) + len(text) + 1 > self.num:
            self.word_list.append(text)
        else:
            if len(self.word_list[-1]) == 0:
                self.word_list[-1] += text
            else:
                self.word_list[-1] = self.word_list[-1] + " " + text

    def end(self):
        for i in self.word_list:
            if len(i) < self.num:
                print(" "*(self.num-len(i)) + i)
            else:
                print(i)

lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()
rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()