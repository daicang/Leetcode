class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        mod = 10**9 + 7

        arr_sum = sum(arr)
        if arr_sum > 0:
            lmax = rmax = arr_sum
            lsum = rsum = 0

            for i, val in enumerate(arr):
                lsum += val
                lmax = max(lmax, lsum)

            i = len(arr) - 1
            while i >= 0:
                rsum += arr[i]
                i -= 1
                rmax = max(rmax, rsum)

            concate_sum = max(lmax, rmax, lmax+rmax)
            result = arr_sum * k

            if k>1 and concate_sum > 2*arr_sum:
                result = result - 2*arr_sum + concate_sum

            return result % mod

        arr = arr + arr
        maxarr = [None] * len(arr)
        maxval = 0

        for i, val in enumerate(arr):
            if i == 0:
                maxarr[i] = val
            else:
                maxarr[i] = max(val, maxarr[i-1]+val)

            maxval = max(maxval, maxarr[i])

        return maxval % mod

s = Solution()

inputs = [
    [[1,2], 3],
    [[1,-2,1], 5],
    [[-1, -2], 7],
    [[-5,-2,0,0,3,9,-2,-5,4], 5]
]

for input in inputs:
    print s.kConcatenationMaxSum(*input)


