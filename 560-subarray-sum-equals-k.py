class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        # counter[s]: number of subarry starting from 0: [0..i] sum to s
        count = 0
        s = 0
        counter = defaultdict(int)
        counter[0] = 1

        for n in nums:
            s += n
            count += counter[s-k]
            counter[s] += 1

        return count

    def subarraySum_scan(self, nums: List[int], k: int) -> int:
        # Time: O(n^2)
        # Space: O(1)
        # TLE
        count = 0
        n = len(nums)
        for start in range(n):
            s = 0
            for end in range(start, n):
                s += nums[end]
                if s == k:
                    count += 1
        return count

    def subarraySum_sumarr(self, nums: List[int], k: int) -> int:
        # Sum array
        # Time: O(n^2)
        # Space: O(n)
        # TLE
        sumarr = []
        s = 0
        for n in nums:
            s += n
            sumarr.append(s)

        count = 0
        for i, val in enumerate(sumarr):
            if val == k:
                count += 1
            for j in range(i):
                if val - sumarr[j] == k:
                    count += 1

        return count