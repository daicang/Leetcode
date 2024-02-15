

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if not s or s[-1] == '1':
            return False

        n = len(s)
        reaches = [False] * n
        reaches[0] = True
        last_jump = 0

        for i in range(n):
            if reaches[i] is False:
                continue
            if i + minJump >= n:
                break
            for j in range(max(last_jump, i+minJump), min(i+maxJump+1, n)):
                if s[j] == '0':
                    reaches[j] = True
            last_jump = i+maxJump

        return reaches[-1]

s = Solution()

data = [
    ['0000000000', 8, 8],
]

for d in data:
    print(s.canReach(*d))
