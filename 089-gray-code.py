class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        results = [0, 1]
        mask = 1
        for _ in range(2, n+1):
            l = len(results)
            mask <<= 1
            for k in range(l-1, -1, -1):
                results.append(results[k]|mask)

        return results

s = Solution()

print s.grayCode(2)

