

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:

    def __init__(self):
        self.arr = []

    def rand10_me(self):
        """
        :rtype: int
        """
        if not self.arr:
            for i in range(10):
                for _ in range(7):
                    self.arr.append(rand7()-1 + i*10)

        val = self.arr.pop()
        return val % 10 + 1

    def rand10(self):
        while True:
            row = rand7()
            col = rand7()
            val = col + (row-1) * 7
            if val <= 40:
                return val % 10 + 1
