class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        asum = sum(A)
        maxsum = 0

        for idx, val in enumerate(A):
            maxsum += idx * val

        lastval = maxsum
        for val in A[::-1]:
            lastval += asum
            lastval -= l * val
            maxsum = max(maxsum, lastval)

        return maxsum
