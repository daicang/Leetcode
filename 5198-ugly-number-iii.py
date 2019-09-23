class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        l = [a, b, c]
        l.sort()
        a, b, c = l

        def gcd(x, y):
            remain = x % y
            while remain != 0:
                x, y = y, remain
                remain = x % y
            return y

        def lcm(x, y):
            if x < y:
                x, y = y, x
            return x * y / gcd(x, y)

        lcm_ab = lcm(a, b)
        lcm_bc = lcm(b, c)
        lcm_ac = lcm(a, c)
        lcm_abc = lcm(lcm_ab, c)

        def unumber_count(u):
            return u/a + u/b + u/c - (u/lcm_ab + u/lcm_bc + u/lcm_ac) + u/lcm_abc

        lower = 0
        upper = n * a

        while lower <= upper:
            middle = (lower + upper) / 2
            count = unumber_count(middle)
            if count == n-1:
                break

            if count < n-1:
                lower = middle + 1
            else:
                upper = middle - 1

        while unumber_count(middle) != n:
            middle += 1

        return middle

s = Solution()

inputs = [
    [3, 2, 3, 5], # 4
    [4, 2, 3, 4], # 6
    [5, 2, 11, 13], # 10
    [14, 3, 7, 13], # 28
    [1000000000, 2, 217983653, 336916467]  # 1999999984
]

for i in inputs:
    print s.nthUglyNumber(*i)

