class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)

        @cache
        def dp(i1, i2):
            if i1 == l1:
                return l2-i2
            if i2 == l2:
                return l1-i1
            if word1[i1] == word2[i2]:
                return dp(i1+1, i2+1)
            return min(dp(i1+1, i2+1), dp(i1, i2+1), dp(i1+1, i2)) + 1

        return dp(0, 0)