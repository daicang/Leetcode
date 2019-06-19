class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        import math

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            nega = True
        else:
            nega = False
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        pow_count = 0
        while divisor <= dividend:
            divisor = divisor << 1
            pow_count += 1

        while True:
            if dividend < divisor:
                divisor = divisor >> 1
                pow_count -= 1
                if pow_count < 0:
                    break
            else:
                # dividend >= divisor
                dividend -= divisor
                quotient += 2**pow_count

        if nega:
            quotient = -quotient
        quotient = min(quotient, 2147483647)
        return quotient


s = Solution()

inputs = [
    (10, 3),
    (1, 1),
    (-1, -1),
    (2147483647, 3)  # 715827882
]

for input in inputs:
    print s.divide(*input)
