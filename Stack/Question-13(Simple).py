# Question 13: Implement two stacks in one array.
class TwoStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top1 = -1
        self.top2 = capacity

    def push1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.array[self.top1] = value
        else:
            print("Stack Overflow")

    def push2(self, value):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.array[self.top2] = value
        else:
            print("Stack Overflow")

    def pop1(self):
        if self.top1 >= 0:
            value = self.array[self.top1]
            self.top1 -= 1
            return value
        else:
            print("Stack Underflow")
            return None

    def pop2(self):
        if self.top2 < self.capacity:
            value = self.array[self.top2]
            self.top2 += 1
            return value
        else:
            print("Stack Underflow")
            return None

ts = TwoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)

print(ts.pop1())
print(ts.pop2())