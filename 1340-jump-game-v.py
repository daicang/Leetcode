from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        if len(arr) == 1:
            return 1

        cache = [None] * len(arr)

        def finished(i):
            if i == 0 and arr[i] <= arr[i+1]:
                return True
            if i == len(arr)-1 and arr[i-1] >= arr[i]:
                return True
            if arr[i-1] >= arr[i] and arr[i+1] >= arr[i]:
                return True
            return False

        def dp(i):
            if i is None:
                return 0

            if cache[i] is not None:
                return cache[i]

            if finished(i):
                return 1

            left_max_idxs = []
            left_max = None
            for j in range(i-1, i-d-1, -1):
                if j < 0 or arr[j] >= arr[i]:
                    break
                if left_max is None or arr[j] > left_max:
                    left_max = arr[j]

            for j in range(i-1, i-d-1, -1):
                if j < 0 or arr[j] >= arr[i]:
                    break
                if arr[j] == left_max:
                    left_max_idxs.append(j)

            right_max_idxs = []
            right_max = None
            for j in range(i+1, i+d+1):
                if j >= len(arr) or arr[j] >= arr[i]:
                    break
                if right_max is None or arr[j] > right_max:
                    right_max = arr[j]

            for j in range(i+1, i+d+1):
                if j >= len(arr) or arr[j] >= arr[i]:
                    break
                if arr[j] == right_max:
                    right_max_idxs.append(j)

            cache[i] = 1 + max([dp(i) for i in left_max_idxs+right_max_idxs])
            return cache[i]

        max_jump = 0
        for i in range(len(arr)):
            # print(arr[i], dp(i))
            max_jump = max(max_jump, dp(i))

        return max_jump

data = [
    [[6,4,14,6,8,13,9,7,10,6,12], 2], # 4
    [[3,3,3,3,3], 3],  # 1
    [[7,6,5,4,3,2,1], 1],  # 7
    [[7,1,7,1,7,1], 2],  # 2
    [[66], 1],  # 1

    [[83,11,83,70,75,45,96,11,80,75,67,83,6,51,71,64,64,42,70,23,11,24,95,65,1,54,31,50,18,16,11,86,2,48,37,34,65,67,4,17,33,70,16,73,57,96,30,26,56,1,16,74,82,77,82,62,32,90,94,33,58,23,23,65,70,12,85,27,38,100,93,49,96,96,77,37,69,71,62,34,4,14,25,37,70,3,67,88,20,30], 29],  # 12
]

s = Solution()

for d in data:
    print(s.maxJumps(*d))

