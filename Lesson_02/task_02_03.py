class AmericanDate:
    def __init__(self, year, month, day):
        self.year = str(year)
        self.month = str(month)
        self.day = str(day)
        if len(self.month) == 1:
            self.month = "0" + self.month
        if len(self.day) == 1:
            self.day = "0" + self.day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        return f"{self.month+'.'+self.day+'.'+self.year}"

class EuropeanDate:
    def __init__(self, year, month, day):
        self.year = str(year)
        self.month = str(month)
        self.day = str(day)
        if len(self.month) == 1:
            self.month = "0" + self.month
        if len(self.day) == 1:
            self.day = "0" + self.day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        return f"{self.day+'.'+self.month+'.'+self.year}"
    
american = AmericanDate(2000, 4, 10)
european = EuropeanDate(2000, 4, 10)
print(american.format())
print(european.format())