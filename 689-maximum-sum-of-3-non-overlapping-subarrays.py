class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        S = []
        num_count = len(nums)
        s = 0

        for i, val in enumerate(nums):
            s += val
            if i >= k:
                s -= nums[i-k]
            if i >= k-1:
                S.append(s)

        left = [0] * len(S)
        right = [0] * len(S)

        best = 0
        for i in range(len(S)):
            if S[i] > S[best]:
                best = i
            left[i] = best

        best = len(S)-1
        for i in range(len(S)-1, -1, -1):
            if S[i] >= S[best]:
                best = i
            right[i] = best

        i1 = i2 = i3 = None
        for mid in range(k, len(S)-k):
            if i1 is None or (S[i1] + S[i2] + S[i3] < S[mid] + S[left[mid-k]] + S[right[mid+k]]):
                i1, i2, i3 = left[mid-k], mid, right[mid+k]

        return i1, i2, i3


s = Solution()

inputs = [
    [[1,2,1,2,6,7,5,1], 2],
    [[1,2,1,2,1,2,1,2,1], 2]
]

for i in inputs:
    print(s.maxSumOfThreeSubarrays(*i))

