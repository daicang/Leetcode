class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator * denominator < 0:
            negative = '-'
        else:
            negative = ''
        numerator = abs(numerator)
        denominator = abs(denominator)

        quotient, r = divmod(numerator, denominator)
        if r == 0:
            return '%s%s' % (negative, quotient)

        remainders = []
        decimals = []
        while r != 0 and r not in remainders:
            remainders.append(r)
            r *= 10
            if r >= denominator:
                q, r = divmod(r, denominator)
                decimals.append(q)
            else:
                decimals.append(0)

        if r == 0:
            decimal = ''.join([str(i) for i in decimals])
            return '%s%s.%s' % (negative, quotient, decimal)

        i = 0
        for i, val in enumerate(remainders):
            if val == r:
                break

        d1 = decimals[:i]
        d1 = [str(i) for i in d1]
        d2 = decimals[i:]
        d2 = [str(i) for i in d2]

        return '%s%s.%s(%s)' % (negative, quotient, ''.join(d1), ''.join(d2))

s = Solution()

data = [
    [1, 2],
    [4, 9],
    [4, 333],
    [-50, 8]
]

for d in data:
    print(s.fractionToDecimal(*d))
