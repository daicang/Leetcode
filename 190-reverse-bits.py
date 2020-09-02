class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str_reversed = bin(n)[2:][::-1]
        result = 0

        for i in range(32):
            result <<= 1
            if i < len(bin_str_reversed) and bin_str_reversed[i] == '1':
                result += 1

        return result