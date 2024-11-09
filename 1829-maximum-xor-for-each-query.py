class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        mval = 2**maximumBit-1
        p = 0

        for n in nums:
            p ^= n
            ans.append(mval ^ p)

        return ans[::-1]
