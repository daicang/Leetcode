class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        while n > 1:
            counter += 1
            if n % 2 == 0:
                n /= 2
            # case (regex).*111011: +1 is better; .*0011: +/-1 are same
            # n = 3(0b11): -1 is better
            elif n > 3 and n % 4 == 3:
                n += 1
            else:
                n -= 1

        return counter

s = Solution()
print s.integerReplacement(100000000)
