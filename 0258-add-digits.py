
class Solution:
    def addDigits(self, num: int) -> int:
        s = 0
        while num > 0:
            q, r = divmod(num, 10)
            s += r
            if s >= 10:
                s -= 9
            num = q

        return s
