
from typing import List

class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:

        # max_end_in(i, k)
        # max_end_in(i, k) = max(max_end_in(prev_i, k-1) + i)
        # max_end_in(i, 0) = i, max_end_in(i, 1) = max(max_end_in(prev_i, 0) + i)

        n = len(receiver)
        prevs = [[] for i in range(n)]

        for i, r in enumerate(receiver):
            prevs[r].append(i)

        last_round = list(range(n))

        for _ in range(k):
            this_round = [None] * n
            for i in range(n):
                for prev in prevs[i]:
                    if last_round[prev] is not None:
                        value = last_round[prev] + i
                        if this_round[i] is None or value > this_round[i]:
                            this_round[i] = value
            last_round = this_round

        return max([x for x in last_round if x is not None])

    def getMaxFunctionValue_binary_lifting(self, receiver: List[int], k: int) -> int:

        bl = k.bit_length()
        n = len(receiver)

        # ends[i][j] is the end point after moving 2^i steps from j
        ends = []

        # profit[i][j] is the value after moving 2^i steps from j
        profit = []

        for _ in range(bl):
            ends.append(receiver[:])
            profit.append(receiver[:])

        for i in range(1, bl):
            for start in range(n):
                # endpoint after 2^i-1 moves from j
                end = ends[i-1][start]
                # calculate new end point
                ends[i][start] = ends[i-1][end]
                # calculate new profit
                profit[i][start] = profit[i-1][start] + profit[i-1][end]

        # Final values starting from i
        values = [i for i in range(n)]

        # Compute values after k iterations
        for bi in range(bl):
            if k & (1<<bi) == 0:
                # skip if bit not set
                continue
            new_values = [None] * n
            for i, val in enumerate(values):
                if val is None:
                    # unreachable
                    continue
                # after 2^bi iteration, end index is ends[bi][start]
                # the values gained is profit[bi][start]
                end = ends[bi][i]
                if new_values[end] is None:
                    new_values[end] = val + profit[bi][i]
                else:
                    new_values[end] = max(new_values[end], val + profit[bi][i])
            values = new_values

        return max([x for x in values if x is not None])



s = Solution()

data = [
    ([0], 1),  # 0
    ([0], 10000000000),  # 0
    ([1,1,1,2,3], 3),  # 10
    ([2,0,1], 4), # 6
]

for d in data:
    # print(s.getMaxFunctionValue(*d))
    print(s.getMaxFunctionValue_binary_lifting(*d))
