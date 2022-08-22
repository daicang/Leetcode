
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        loc1 = []
        loc2 = []

        for i, w in enumerate(wordsDict):
            if w == word1:
                loc1.append(i)
            elif w == word2:
                loc2.append(i)

        if word1 == word2:
            shortest = loc1[1] - loc1[0]
            for i, val in enumerate(loc1):
                if i >= 1:
                    shortest = min(shortest, loc1[i]-loc1[i-1])
            return shortest

        i1 = 0
        i2 = 0
        shortest = abs(loc1[0]-loc2[0])

        while i1 < len(loc1) and i2 < len(loc2):
            shortest = min(shortest, abs(loc1[i1]-loc2[i2]))
            if loc1[i1] < loc2[i2]:
                i1 += 1
            else:
                i2 += 1

        return shortest
