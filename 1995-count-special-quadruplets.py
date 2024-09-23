class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        s1 = defaultdict(int)
        s2 = defaultdict(int)
        s3 = defaultdict(int)
        count = 0

        for n in nums:
            count += s3[n]
            for s in s2.keys():
                s3[s+n] += s2[s]
            for s in s1.keys():
                s2[s+n] += s1[s]
            s1[n] += 1

        return count
