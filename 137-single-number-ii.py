from typing import List

class Solution:
    def singleNumber_add(self, nums: List[int]) -> int:
        positive = True
        positives = []
        negatives = []
        for n in nums:
            if n >= 0:
                positives.append(n)
            else:
                negatives.append(-n)

        if len(positives) % 3 == 0:
            positive = False
            nums = negatives
        else:
            nums = positives

        def three_add(l, n):
            # convert to k-based digits, low to high
            idx = 0
            while n > 0:
                l[idx] = (l[idx] + (n % 3)) % 3
                n //= 3
                idx += 1

        l = [0] * 30  # n be less than 3^30
        for n in nums:
            three_add(l, n)

        # Conver to 10-based
        val = 0
        for i in l[::-1]:
            val *= 3
            val += i
        if not positive:
            val *= -1
        return val


    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for n in nums:
            seen_once = ~seen_twice & (seen_once^n)
            seen_twice = ~seen_once & (seen_twice^n)
        # print(seen_once, seen_twice)
        return seen_once

data = [
    [-2,-2,1,1,4,1,4,4,-4,-2],  # -4
    [2,2,3,2],  # 3
    [0,1,0,1,0,1,99],  # 99
    [1,1,1,3,3,3,5]  # 5
]

s = Solution()

for d in data:
    print(s.singleNumber_add(d))
