
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n:
            last_bit = n & 1
            if last_bit:
                return n == 1
            n >>= 1
