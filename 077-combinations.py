class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        from copy import copy
        combines = []

        def backtrack(start, numleft, l):
            if numleft == 0:
                combines.append(copy(l))
                return
            if start > n:
                return
            backtrack(start+1, numleft, l)
            l.append(start)
            backtrack(start+1, numleft-1, l)
            l.pop()

        backtrack(1, k, [])
        return combines


s = Solution()

inputs = [
    [4, 2],
]

for i in inputs:
    print s.combine(*i)

