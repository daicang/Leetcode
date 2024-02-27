

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # quicksort, TLE
        def _sort(lo, hi):
            if lo >= hi:
                return

            pivot = nums[lo]
            first_ge_idx = lo

            for i in range(lo+1, hi+1):
                if nums[i] < pivot:
                    # switch with arr[first_ge_idx]
                    first_ge_idx += 1
                    nums[i], nums[first_ge_idx] = nums[first_ge_idx], nums[i]

            nums[lo], nums[first_ge_idx] = nums[first_ge_idx], nums[lo]

            _sort(lo, first_ge_idx-1)
            _sort(first_ge_idx+1, hi)

        _sort(0, len(nums)-1)
        return nums


    def sortArray_merge(self, nums: List[int]) -> List[int]:
        def _sort(lo, hi):
            # normal merge sort, O(n) extra space, AC
            if hi <= lo:
                return

            mid = (lo+hi) // 2
            _sort(lo, mid)
            _sort(mid+1, hi)

            arr1 = nums[lo:mid+1]
            arr2 = nums[mid+1:hi+1]

            i = lo
            p1 = 0
            p2 = 0
            l1 = len(arr1)
            l2 = len(arr2)

            while p1 < l1 and p2 < l2:
                if arr1[p1] < arr2[p2]:
                    nums[i] = arr1[p1]
                    p1 += 1
                else:
                    nums[i] = arr2[p2]
                    p2 += 1
                i += 1

            for j in range(p1, l1):
                nums[i] = arr1[j]
                i += 1
            for j in range(p2, l2):
                nums[i] = arr2[j]
                i += 1


        def _sort_in_place(lo, hi):
            # in-place merge sort, TLE
            if hi <= lo:
                return

            mid = (hi + lo) // 2
            _sort(lo, mid)
            _sort(mid+1, hi)

            # merge
            p1 = lo
            p2 = mid+1

            while p1 <= mid and p2 <= hi:
                if nums[p1] <= nums[p2]:
                    p1 += 1
                else:
                    # put n[p2] in n[p1], shifting elements[p1,p2] to righy by 1
                    val = nums[p2]
                    for i in range(p2, p1, -1):
                        nums[i] = nums[i-1]
                    nums[p1] = val

                    p1 += 1
                    mid += 1
                    p2 += 1

            return

        _sort(0, len(nums)-1)

        return nums


s = Solution()

data = [
    [5,2,3,1],
    [5,1,1,2,0,0],
]

for d in data:
    print(s.sortArray(d))
