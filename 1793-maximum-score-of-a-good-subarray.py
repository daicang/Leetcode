from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = k
        right = k
        max_score = nums[k]
        min_height = nums[k]

        while right-left+1 < len(nums):
            if left == 0:
                # expand right
                right += 1
                min_height = min(min_height, nums[right])
                max_score = max(max_score, min_height*(right-left+1))
            elif right == len(nums)-1:
                # expand left
                left -= 1
                min_height = min(min_height, nums[left])
                max_score = max(max_score, min_height*(right-left+1))
            elif nums[left-1] >= nums[right+1]:
                # expand left
                left -= 1
                min_height = min(min_height, nums[left])
                max_score = max(max_score, min_height*(right-left+1))
            else:
                # expand right
                right += 1
                min_height = min(min_height, nums[right])
                max_score = max(max_score, min_height*(right-left+1))

        return max_score

s = Solution()

data = [
    ([1,4,3,7,4,5], 3), # 15
    ([6569,9667,3148,7698,1622,2194,793,9041,1670,1872], 5),  # 9732
]

for d in data:
    print(s.maximumScore(*d))
