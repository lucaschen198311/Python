class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for el in nums:
            self.result += el
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for el in nums:
            self.result -= el
        return self
# create an instance:
md = MathDojo()
test1 = MathDojo()
test2 = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
y = test1.add(2,3,4).add(2,5,1).subtract(3).result
z = test2.add(2,1,10).add(2,5).subtract(3,2,7,9).result
print(x, y, z) # should print 5
# run each of the methods a few more times and check the result!