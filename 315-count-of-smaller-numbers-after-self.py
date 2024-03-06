# 315-count-of-smaller-numbers-after-self.py
# Difficulty: hard

from typing import List


class SegmentTree:

    def __init__(self, size):
        self.size = size
        self.tree = [0] * (2*size)

    def update(self, index, value):
        index = index + self.size
        self.tree[index] += value
        while index > 1:
            index = index // 2
            self.tree[index] = self.tree[index*2] + self.tree[index*2+1]

    def query(self, left, right):
        # return sum of [left, right)
        result = 0
        left = left + self.size
        right = right + self.size
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            left //= 2
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            right //= 2
        return result

class Solution:
    def countSmaller_segtree(self, nums: List[int]) -> List[int]:
        offset = 10**4  # offset negative values
        size = 2 * 10**4 + 1  # total possible values in nums
        tree = SegmentTree(size)

        result = []

        for num in reversed(nums):
            n = num + offset
            result.append(tree.query(0, n))
            tree.update(n, 1)

        return result[::-1]


    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = [0] * n

        def merge_sort(arr, lo, hi):
            if hi-lo < 2:
                return
            mid = (lo+hi) // 2
            merge_sort(arr, lo, mid)
            merge_sort(arr, mid, hi)

            # merge
            arr1 = arr[lo:mid]
            arr2 = arr[mid:hi]
            p1 = p2 = 0
            i = lo

            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1][0] <= arr2[p2][0]:
                    arr[i] = arr1[p1]
                    counter[arr1[p1][1]] += p2
                    p1 += 1
                    i += 1
                else:
                    arr[i] = arr2[p2]
                    p2 += 1
                    i += 1
            for j in range(p1, len(arr1)):
                counter[arr1[j][1]] += len(arr2)
                arr[i] = arr1[j]
                i += 1
            for j in range(p2, len(arr2)):
                arr[i] = arr2[j]
                i += 1

        arr = []
        for i, val in enumerate(nums):
            arr.append((val, i))

        merge_sort(arr, 0, n)
        return counter

# class Solution(object):
#     def countSmaller(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         def mergesort(arr):
#             l = len(arr)
#             if l < 2: return arr
#             mid = l / 2
#             left, right = mergesort(arr[:mid]), mergesort(arr[mid:])

#             for i in range(l)[::-1]:
#                 if not right or left and left[-1][1] > right[-1][1]:
#                     smaller[left[-1][0]] += len(right)
#                     arr[i] = left.pop()
#                 else:
#                     arr[i] = right.pop()

#             return arr

#         smaller = [0] * len(nums)
#         mergesort(list(enumerate(nums)))

#         return smaller

s = Solution()

data = [
    [5,2,6,1],
    [5,2,0,1,3],
    [-1,-1]
]

for d in data:
    print(s.countSmaller(d))
