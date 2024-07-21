class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        count = 0
        for i, val in enumerate(target):
            if i == 0:
                count += val
            else:
                if val > target[i-1]:
                    count += val - target[i-1]
        return count
