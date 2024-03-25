class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day
        self.all_day = month*30+day

    def __sub__(self, other):
        if self.month == other.month and self.day == other.day:
            return 0
        else:
            return self.all_day - other.all_day

jan5 = Date(1, 5)
jan1 = Date(1, 1)

print(jan5 - jan1)
print(jan1 - jan5)
print(jan1 - jan1)
print(jan5 - jan5)