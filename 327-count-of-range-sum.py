# 327-count-of-range-sum.py

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # Start: inclusive
        # End: exclusive
        def iter(start, end):
            if end - start <= 1: return 0
            mid = (start + end) / 2
            count = iter(start, mid) + iter(mid, end)
            cache = [0] * (end - start)
            j = k = t = mid
            r = 0
            for i in xrange(start, mid):
                # j: First index that sum[i, j] >= lower
                # k: First index that sum[i, k] >  upper
                # This is merge sort, so no available value after k,
                # and we use t/cache to sort it.
                while j < end and sum[j] - sum[i] < lower: j += 1
                while k < end and sum[k] - sum[i] <= upper: k += 1
                while t < end and sum[t] < sum[i]:
                    cache[r] = sum[t]
                    t += 1
                    r += 1
                cache[r] = sum[i]
                r += 1
                count += k - j
            for i in xrange(r): sum[start+i] = cache[i]
            return count

        l = len(nums)
        sum = [0]*(l+1)
        for i in xrange(1, l+1): sum[i] = sum[i-1] + nums[i-1]
        return iter(0, l+1)

s = Solution()
print s.countRangeSum([-2, 5, -1], -2, 2)
