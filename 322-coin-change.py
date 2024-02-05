
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [None] * (amount+1)
        memo[0] = 0
        coins.sort()

        def get_min_change(amount):
            if memo[amount] is None:
                min_change = False
                for c in coins:
                    r = amount - c
                    if r < 0:
                        break
                    change = get_min_change(r)
                    if change is not False:
                        if min_change is False:
                            min_change = change+1
                        else:
                            min_change = min(min_change, change+1)
                memo[amount] = min_change
            return memo[amount]

        change = get_min_change(amount)
        if change is False:
            return -1
        return change


data = [
    [[2], 3],
]

s = Solution()

for d in data:
    print(s.coinChange(*d))
