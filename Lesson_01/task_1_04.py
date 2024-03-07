class OddEvenSeparator():
    def __init__(self):
        self.num_list = list()
        
    def add_number(self, num):
        self.num_list.append(num)
    
    def even(self):
        self.num_even = [i for i in self.num_list if i % 2 == 0]
        return self.num_even
    
    def odd(self):
        self.num_odd = [i for i in self.num_list if i %2 == 1]
        return self.num_odd
            
separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(4)
separator.add_number(5)
separator.even()
separator.odd()
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))
