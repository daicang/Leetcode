from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # [2^i, 2^(i+1)]
        buckets = []
        for _ in range(10):
            buckets.append(set())

        def get_log(i):
            log = 0
            i = abs(i)
            while i > 1:
                i >>= 1
                log += 1
            return log

        zero_count = 0
        for i in arr:
            if i == 0:
                zero_count += 1
            else:
                buckets[get_log(i)].add(i)

        if zero_count > 1:
            return True

        for i in range(len(buckets)-1):
            for j in buckets[i]:
                if 2*j in buckets[i+1]:
                    return True
        return False

s = Solution()

data = [
    [10,2,5,3],
    [7,1,14,11],
    [3,1,7,11],
    [0,0],
    [-10,12,-20,-8,15]
]

for d in data:
    print(s.checkIfExist(d))

