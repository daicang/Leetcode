class Solution:
    def maxOperations(self, s: str) -> int:
        ops = 0
        zeros = 0
        s = s[::-1]
        dup_zero = False
        for i, ch in enumerate(s):
            if ch == '1':
                ops += zeros
                dup_zero = False
            else:
                if not dup_zero:
                    zeros += 1
                    dup_zero = True

        return ops