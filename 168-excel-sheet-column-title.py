class Solution:
    def convertToTitle(self, n: int) -> str:
        result = []
        bits = 1
        m = n
        while True:
            m -= 26**bits
            if m > 0:
                bits += 1
            else:
                break

        for _ in range(bits):
            # 1-26 => A-Z
            result.append(chr(ord('A') + ((n-1) % 26)))
            n -= (n-1)%26+1
            n //= 26

        return ''.join(result[::-1])

s = Solution()

data = [
    1,
    26,
    28,
    701,
    52, # AZ
]
for d in data:
    print(s.convertToTitle(d))