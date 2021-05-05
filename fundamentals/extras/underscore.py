class Underscore:
    def map(self, iterable, callback):
        return list(map(callback,iterable))
    
    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if callback(iterable[i]):
                return iterable[i]
            
    def filter(self, iterable, callback):
        return list(filter(callback,iterable))
    
    def reject(self, iterable, callback):
        arr = []
        for i in range(len(iterable)):
            if callback(iterable[i]) == False:
                arr.append(iterable[i])
        return arr
        
_ = Underscore()
a = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(a)
b = _.map([1,2,3], lambda x: x*2) # should return [2,4,6]
print(b)
c = _.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
print(c)
d = _.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
print(d)
e = _.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]
print(e)



