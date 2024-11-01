class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def traverse(i, k, nums):
            if k == 0 and sum(nums) == n:
                result.append(nums[:])
                return
            for j in range(i, 10):
                nums.append(j)
                traverse(j+1, k-1, nums)
                nums.pop()

        traverse(1, k, [])
        return result
