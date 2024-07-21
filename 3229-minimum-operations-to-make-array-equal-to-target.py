class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        arr = [0] * n
        for i in range(n):
            arr[i] = target[i] - nums[i]

        arr = [0] + arr + [0]
        ops = 0
        for i, val in enumerate(arr):
            if i == 0:
                continue
            else:
                if val > arr[i-1]:
                    ops += val - arr[i-1]

        return ops