class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c1, c2 = 0, 0
        for b in bills:
            if b == 5:
                c1 += 1
            elif b == 10:
                if c1 == 0:
                    return False
                c1 -= 1
                c2 += 1
            else:
                if c2 > 0:
                    if c1 == 0:
                        return False
                    c2 -= 1
                    c1 -= 1
                else:
                    if c1 < 3:
                        return False
                    c1 -= 3

        return True
