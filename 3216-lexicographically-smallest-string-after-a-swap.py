class Solution:
    def getSmallestString(self, s: str) -> str:
        i = 0
        found = False
        result = [ch for ch in s]
        for i in range(len(s)-1):
            d1, d2 = int(s[i]), int(s[i+1])
            if d1 % 2 == d2 % 2 and d1 > d2:
                found = True
                break
        if found:
            result[i], result[i+1] = result[i+1], result[i]
        return ''.join(result)
