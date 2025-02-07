class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 2
        while i <= sqrt(c):
            q, r = divmod(c, i)
            if r == 0:
                c = q
                count = 1
                while c % i == 0:
                    count += 1
                    c /= i
                if i % 4 == 3 and count % 2 != 0:
                    return False
            i += 1
        return c % 4 != 3

    def judgeSquareSum_1(self, c: int) -> bool:
        if c == 0: return True

        def check(low, high, b):
            if low > high:
                return False
            mid = (low+high) // 2
            p = mid * mid
            if p == b:
                return True
            elif p < b:
                return check(mid+1, high, b)
            else:
                return check(low, mid-1, b)

        a = 0
        while True:
            p = a * a
            if p >= c:
                break
            b = c - p
            if check(1, b, b):
                return True
            a += 1
        return False
