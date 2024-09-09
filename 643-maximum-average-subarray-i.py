class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        back = 0
        s = 0
        max_s = None
        for i, n in enumerate(nums):
            s += n
            length = i - back + 1
            while length > k:
                s -= nums[back]
                back += 1
                length -= 1
            if length == k:
                if max_s is None:
                    max_s = s
                else:
                    max_s = max(max_s, s)
        return max_s / k
