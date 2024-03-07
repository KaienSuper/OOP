class MinMaxWordFinder():
    def __init__(self):
        self.sentences_list = list()
        self.shortest_words_list = list()
        self.longest_words_list = list()
    def add_sentence(self, text):
        text1 = text.split(" ")
        for i in text1:
            self.sentences_list.append(i)

    def shortest_words(self):
        for i in self.sentences_list:
            for j in self.sentences_list:
                if len(i) <= len(j):
                    point = True
                else:
                    point = False
                    break
            if point == True:
                self.shortest_words_list.append(i)
        self.shortest_words_list.sort()
        return self.shortest_words_list
    
    def longest_words(self):
        for i in self.sentences_list:
            for j in self.sentences_list:
                if len(i) >= len(j):
                    point = True
                else:
                    point = False
                    break
            if point == True:
                if i not in self.longest_words_list:
                    self.longest_words_list.append(i)
        self.longest_words_list.sort()
        return self.longest_words_list
    
finder = MinMaxWordFinder()
finder.add_sentence('hello abc world')
finder.add_sentence('def asdf qwert hello')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))