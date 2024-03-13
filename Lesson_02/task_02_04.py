class MinStat:
    def __init__(self):
        self.nums = list()

    def add_number(self, nums):
        self.nums.append(nums)

    def result(self):
        if len(self.nums) > 0:
            return min(self.nums)
        else:
            return None

class MaxStat:
    def __init__(self):
        self.nums = list()

    def add_number(self, nums):
        self.nums.append(nums)

    def result(self):
        if len(self.nums) > 0:
            return max(self.nums)
        else:
            return None

class AverageStat:
    def __init__(self):
        self.nums = list()

    def add_number(self, nums):
        self.nums.append(nums)

    def result(self):
        res = 0
        for i in self.nums:
            res += i
        if len(self.nums) > 0:
            return res/len(self.nums)
        else:
            return None
values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())