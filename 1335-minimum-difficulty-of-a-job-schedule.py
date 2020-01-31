from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        size = len(jobDifficulty)
        cache = {}

        def bfs(start, d_remain):
            if d_remain == 0:
                return -1
            if d_remain == 1:
                return max(jobDifficulty[start:])

            key = (start, d_remain)
            if key in cache:
                return cache[key]

            score = None
            peak = None
            d_remain -= 1

            for i in range(start, size-d_remain):
                if peak is None or jobDifficulty[i] > peak:
                    peak = jobDifficulty[i]

                score_left = bfs(i+1, d_remain)
                if score_left == -1:
                    continue

                score = min(score, peak+score_left) if score else peak+score_left

            if score is None:
                score = -1

            cache[key] = score
            return score

        return bfs(0, d)


s = Solution()

data = [
    [[6,5,4,3,2,1], 2],  #7
    [[9, 9, 9], 4],  #-1
    [[1,1,1], 3],  #3
    [[7,1,7,1,7,1], 3], # 15
    [[11,111,22,222,33,333,44,444], 6]  # 843
]

for d in data:
    print(s.minDifficulty(*d))
