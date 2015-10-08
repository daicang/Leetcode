#!/usr/bin/python

class Solution(object):
    def maxSubArray(self, nums):
        arr = [None] * len(nums)
        arr[0], ret = nums[0], nums[0]
        for i in range(1, len(nums)):
            arr[i] = max(nums[i], arr[i-1] + nums[i])
            ret = max(ret, arr[i])
        return ret

