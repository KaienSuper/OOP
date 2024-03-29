class Polynomial:
    def __init__(self, coefficients):
        if 3 > len(coefficients):
            self.a = 0
        else:
            self.a = coefficients[2]
        self.b = coefficients[1]
        self.c = coefficients[0]
    
    def poly(self, x):
        return (x^2)*self.a + self.b*x + self.c
    
    def __add__(self, other):
        return Polynomial(self.c + other.c, self.b + other.b, self.a + other.a)
    
# Ваш код

poly = Polynomial([10, -1])
print(poly(0))
print(poly(1))
print(poly(2))