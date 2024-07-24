
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Sliding window
        # Time: O(nlog(n))
        # Space: O(1)
        nums.sort()
        head, tail = 0, 0
        freq = 1
        room = 0
        for head in range(1, len(nums)):
            room += (head-tail) * (nums[head]-nums[head-1])
            while room > k:
                room -= nums[head] - nums[tail]
                tail += 1
            freq = max(freq, head-tail+1)

        return freq
