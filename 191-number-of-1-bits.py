class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_str = bin(n)[2:]
        result = 0
        for ch in bin_str:
            if ch == '1':
                result += 1
        return result