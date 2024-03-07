class Balance():
    def __init__(self):
        self.right_mass = 0
        self.left_mass = 0
        
    def add_right(self, mass):
        self.right_mass += mass
    
    def add_left(self, mass):
        self.left_mass += mass
    
    def result(self):
        if self.right_mass == self.left_mass:
            return "="
        elif self.right_mass > self.left_mass:
            return "R"
        else:
            return "L"

balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(1)
print(balance.result())