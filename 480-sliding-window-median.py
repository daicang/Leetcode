
import bisect

from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        medians = []
        window = []  # Sorted values in window

        for i in range(k):
            window.append(nums[i])
        window.sort()

        if k % 2 == 0:
            # 0 1 2 3
            medians.append((window[k//2]+window[k//2-1])/2)
        else:
            # 0 1 2
            medians.append(window[k//2])

        for new_start in range(1, n-k+1):
            # pop leaving number
            pos = bisect.bisect_left(window, nums[new_start-1])
            del window[pos]
            # insert new number
            new_idx = new_start+k-1
            new_num = nums[new_idx]
            pos = bisect.bisect_left(window, new_num)
            window.insert(pos, new_num)

            if k % 2 == 0:
                # 0 1 2 3
                medians.append((window[k//2]+window[k//2-1])/2)
            else:
                # 0 1 2
                medians.append(window[k//2])

        return medians


data = [
    [[1,3,-1,-3,5,3,6,7], 3],
]

s = Solution()

for d in data:
    print(s.medianSlidingWindow(*d))
