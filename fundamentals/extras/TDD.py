import unittest

def reverseList(input):
    return input[::-1]

def isPalindrome(input):
    for i in range(0,len(input)//2):
        if input[i] != input[len(input)- 1 -i]:
            return False
    return True

def factorial(n):
    if n<1:
        return 
    if n ==1:
        return n
    return n*factorial(n-1)

def fibonacci(n):
    if n>=0 and n<=1:
        return n
    elif n>1:
        fibNum=fibonacci(n-1) + fibonacci(n-2)
    return fibNum;

class isPalindromeTests(unittest.TestCase):
    def testTrue(self):
        self.assertEqual(isPalindrome("racecar"), True)
        # another way to write above is
        self.assertTrue(isPalindrome("racecar"))
    def testFalse(self):
        self.assertEqual(isPalindrome("rabcr"), False)
        # another way to write above is
        self.assertFalse(isPalindrome("rabcr"))
    # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

class fibonacciTests(unittest.TestCase):
    def testTrue(self):
        self.assertEqual(fibonacci(5), 5)
        # another way to write above is
        #self.assertTrue(fibonacci(5))
    def testFalse(self):
        self.assertEqual(fibonacci(6), 8)
        # another way to write above is
        #self.assertFalse(fibonacci("rabcr"))
    # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")
        
class factorialTests(unittest.TestCase):
    def testTrue(self):
        self.assertEqual(factorial(5), 120)
        # another way to write above is
        #self.assertTrue(fibonacci(5))
    def testFalse(self):
        self.assertEqual(factorial(6), 720)
        # another way to write above is
        #self.assertFalse(fibonacci("rabcr"))
    # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")
        

class reverseListTests(unittest.TestCase):
    def testTrue(self):
        self.assertEqual(reverseList("abc"), "cba")
        # another way to write above is
        #self.assertTrue(fibonacci(5))
    def testFalse(self):
        self.assertEqual(reverseList("a"), "a")
        # another way to write above is
        #self.assertFalse(fibonacci("rabcr"))
    # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")


        
print(__name__)
        
if __name__ == '__main__':
    unittest.main() # this runs our tests
