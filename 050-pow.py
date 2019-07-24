class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1.0/x

        bitmap = []
        while n != 0:
            n, remain = divmod(n, 2)
            bitmap.append(remain)

        ans = 1
        for val in bitmap:
            if val:
                ans *= x
            x *= x

        return ans


s = Solution()
inputs = [
    [3, 5],
    [2, 10],
    [3, 0],
    [3, -1]
]
for input in inputs:
    print s.myPow(*input)

