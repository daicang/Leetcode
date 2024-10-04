class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # Fenwick tree
        count = 0
        n = len(nums1)
        ids = [0] * n
        ftree = [0] * (n+1)

        def fenwick_add(i, val):
            j = i+1
            while j <= n:
                ftree[j] += val
                j += j & (-j)

        def fenwick_sum(i):
            s = 0
            j = i + 1
            while j > 0:
                s += ftree[j]
                j -= j & (-j)
            return s

        for i, val in enumerate(nums2):
            ids[val] = i
        for i in range(n-1):
            mid_id = ids[nums1[i]]
            smaller = fenwick_sum(mid_id)
            larger = n-1 - mid_id - (i-smaller)
            count += smaller * larger
            fenwick_add(mid_id, 1)

        return count
