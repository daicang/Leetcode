
# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return True

class Solution:
    def findCelebrity(self, n: int) -> int:
        cand = 0
        for i in range(1, n):
            if knows(cand, i) or not knows(i, cand):
                cand = i

        for i in range(n):
            if cand != i:
                if knows(cand, i) or not knows(i, cand):
                    return -1
        return cand
