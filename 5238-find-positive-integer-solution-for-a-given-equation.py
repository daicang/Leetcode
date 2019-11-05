"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        solutions = []
        y = 1000

        for x in range(1, 1001):
            while y > 0:
                val = customfunction.f(x, y)
                if val == z:
                    solutions.append([x, y])
                    break

                elif val < z:
                    break

                else:  # val > z, decrease y
                    y -= 1
            if y == 0:
                break

        return solutions



