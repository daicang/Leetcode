# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    pass

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 0, n
        mid = (low + high) / 2
        ans = guess(mid)
        while ans:
            if ans == -1:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low + high) / 2
            ans = guess(mid)

        return mid
