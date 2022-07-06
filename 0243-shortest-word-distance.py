class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_dist = -1
        i1 = i2 = -1
        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
                if i2 != -1:
                    if min_dist == -1:
                        min_dist = i1 - i2
                    else:
                        min_dist = min(min_dist, i1-i2)

            if word == word2:
                i2 = i
                if i1 != -1:
                    if min_dist == -1:
                        min_dist = i2-i1
                    else:
                        min_dist = min(min_dist, i2-i1)

        return min_dist
