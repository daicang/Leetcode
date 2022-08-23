
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        pairs = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }
        count = 0

        def dfs(left, right, s):
            nonlocal count
            if left > right:
                if len(s) > 1 and s[0] == '0': return
                val = int(''.join(s))
                if val >= int(low) and val <= int(high):
                    count += 1
                return

            for l, r in pairs.items():
                if left == right:
                    if l != r: continue
                available[left] = l
                available[right] = r
                dfs(left+1, right-1, available)

        for width in range(len(low), len(high)+1):
            available = [''] * width
            dfs(0, width-1, available)

        return count


s = Solution()

inputs = [
    ['50', '100'],
    ['0', '0'],
]

for i in inputs:
    print(s.strobogrammaticInRange(*i))
