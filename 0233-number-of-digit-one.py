
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        s = str(n)
        power = 1

        i = len(s)-1
        while i >= 0:
            val = int(s[i])

            if i > 0:
                next_val = int(s[:i])
                count += next_val * power

            if val == 1:
                count += 1
                if i != len(s)-1:
                    count += int(s[i+1:])
            elif val > 1:
                count += power

            power *= 10
            i -= 1

        return count


s = Solution()

inputs = [
    [13, 6],
    [0, 0],
    [100, 21],
    [1000, 301],
]

for i in inputs:
    result = s.countDigitOne(i[0])
    if result != i[1]:
        print('%s expect %s got %s' % (i[0], i[1], result))
