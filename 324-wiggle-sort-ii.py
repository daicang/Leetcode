class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = ceil(len(nums)/2)
        nums[::2], nums[1::2] = nums[:half:][::-1], nums[half::][::-1]

    def wiggleSort(self, nums: List[int]) -> None:
        # Index mapping, 3-way partition
        # Time: O(n)
        def quick_find(lo, hi, k):
            pivot = nums[hi]
            j = lo
            for i in range(lo, hi):
                if nums[i] < pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    j += 1
            nums[j], nums[hi] = nums[hi], nums[j]
            if j == k:
                return nums[j]
            elif j < k:
                return quick_find(j+1, hi, k)
            else:
                return quick_find(lo, j-1, k)

        midval = quick_find(0, len(nums)-1, len(nums)//2)

        # index mapping
        def vi(i):
            mid = len(nums) // 2
            if i < mid:
                # map to high index
                return 2*i + 1
            else:
                # map to low index
                return (i-mid) * 2

        # 3-way partition
        # https://en.wikipedia.org/wiki/Dutch_national_flag_problem#Pseudocode
        i, j, k = 0, 0, len(nums)-1
        while j <= k:
            if nums[vi(j)] > midval:
                nums[vi(j)], nums[vi(i)] = nums[vi(i)], nums[vi(j)]
                i += 1
                j += 1
            elif nums[vi(j)] < midval:
                nums[vi(j)], nums[vi(k)] = nums[vi(k)], nums[vi(j)]
                k -= 1
            else:
                j += 1
