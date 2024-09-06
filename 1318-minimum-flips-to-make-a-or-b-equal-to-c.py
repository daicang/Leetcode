class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0

        while c:
            c, rc = divmod(c, 2)
            a, ra = divmod(a, 2)
            b, rb = divmod(b, 2)
            if rc == 0:
                count += ra + rb
            else:
                if ra == 0 and rb == 0:
                    count += 1

        while a:
            a, ra = divmod(a, 2)
            count += ra

        while b:
            b, rb = divmod(b, 2)
            count += rb

        return count
