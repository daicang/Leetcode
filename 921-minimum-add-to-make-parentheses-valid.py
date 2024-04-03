

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        rparen = 0
        count = 0

        for ch in s:
            if ch == '(':
                rparen += 1
            else:
                if rparen:
                    rparen -= 1
                else:
                    count += 1

        return count + rparen