
class Solution:
    def minInsertions(self, s: str) -> int:
        rparen = 0
        count = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                rparen += 1
            else:
                if i < len(s)-1 and s[i+1] == ')':
                    # ))
                    if rparen:
                        rparen -= 1
                    else:
                        # insert (
                        count += 1
                    i += 1
                else:
                    # )
                    if rparen > 0:
                        # insert )
                        count += 1
                        rparen -= 1
                    else:
                        # insert ()
                        count += 2
            i += 1

        return count + 2*rparen
