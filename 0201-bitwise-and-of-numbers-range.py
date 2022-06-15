class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        v1: int = left & right
        v2: int = left | right
        shift: int = 0
        i: int = 0

        while v1 > 0 or v2 > 0:
            if v1 % 2 != v2 % 2:
                shift = i
            i += 1

            v1 >>= 1
            v2 >>= 1

        result = (left & right) >> shift
        result <<= shift
        return result


s = Solution()

inputs = [
    (5, 7),
    (0, 0),
    (1, 2147483647),
    (3, 3)
]

for i in inputs:
    print(s.rangeBitwiseAnd(i[0], i[1]))
