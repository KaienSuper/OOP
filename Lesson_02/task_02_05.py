class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.nums_dict = {}

    def get_value(self, row, col):
        if row > self.rows and col > self.cols:
            return None
        elif (row, col) not in self.nums_dict:
            return 0
        else:
            return self.nums_dict[(row, col)]

    def set_value(self, row, col, value):
        if row <= self.rows and col <= self.cols:
            self.nums_dict[(row, col)] = value

    def n_rows(self):
        return self.rows
    
    def n_cols(self):
        return self.cols


tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
