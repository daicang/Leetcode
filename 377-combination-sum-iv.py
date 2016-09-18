class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def _iter(t, cache):
            if t in cache:
                return cache[t]

            ret = 0
            for num in nums:
                if num <= t:
                    ret += _iter(t-num, cache)
            cache[t] = ret
            return ret

        cache = {0: 1}
        return _iter(target, cache)

s = Solution()
print s.combinationSum4([1,2,3], 4)
