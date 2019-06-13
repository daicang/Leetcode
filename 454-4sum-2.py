class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import defaultdict
        sums = defaultdict(int)
        count = 0

        for a in A:
            for b in B:
                sums[-(a+b)] += 1

        for c in C:
            for d in D:
                s = c + d
                if s in sums:
                    count += sums[s]

        return count
