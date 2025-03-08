class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # Count 1-3-2-4 pattern
        n = len(nums)
        count = 0
        count_3 = [0] * n  # 1-3-2 pattern
        for j in range(n):
            count_1 = 0  # 1-2 pattern
            for i in range(j):
                if nums[i] < nums[j]:
                    # up, could be 1-2 or 3-4
                    count_1 += 1
                    count += count_3[i]
                elif nums[i] > nums[j]:
                    # down, could be 3-2
                    count_3[i] += count_1
        return count

    def countQuadruplets(self, nums: List[int]) -> int:
        # Time: O(n^2log(n))
        # Space: O(n)
        n = len(nums)
        sl = [nums[0]]
        count = 0

        for j in range(1, n):
            bisect.insort(sl, nums[j])
            if nums[j] < nums[-1]:
                c = 1
            else:
                c = 0
            for k in range(n-2, j, -1):
                if nums[k] > nums[j]:
                    c += 1
                else:
                    # how many numbers lower than k (from bisect)
                    # times how many numbers larger than j
                    count += bisect_left(sl, nums[k]) * c

        return count
