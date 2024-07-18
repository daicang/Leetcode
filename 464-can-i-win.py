class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if (maxChoosableInteger * (1+maxChoosableInteger)) // 2 < desiredTotal:
            return False

        cache = {}
        def win(n, numbers):
            if numbers in cache:
                return cache[numbers]
            if numbers and numbers[-1] > n:
                return True
            for i, val in enumerate(numbers):
                # if opponent loses for any move, we win
                r = n - val
                if r <= 0:
                    cache[numbers] = True
                    return True
                if win(r, numbers[:i]+numbers[i+1:]) == False:
                    cache[numbers] = True
                    return True
            # none of the move can win
            cache[numbers] = False
            return False

        return win(desiredTotal, tuple(i for i in range(1, maxChoosableInteger+1)))
