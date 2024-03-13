class Selector():
    def __init__(self, nums):
        self.nums_list = nums
    
    def get_odds(self):
        odds_list = [i for i in self.nums_list if i % 2 == 1]
        return odds_list
    
    def get_evens(self):
        evens_list = [i for i in self.nums_list if i % 2 == 0]
        return evens_list
    
values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))