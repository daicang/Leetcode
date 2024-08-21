class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        for i, arr in enumerate(arrays):
            if i == 0:
                minval = arr[0]
                maxval = arr[-1]
            else:
                res = max(res, arr[-1]-minval, maxval-arr[0])
                minval = min(minval, arr[0])
                maxval = max(maxval, arr[-1])
        return res
