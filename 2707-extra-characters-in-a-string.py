class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        n = len(s)
        dp = [n] * (n+1)

        for i in range(n):
            target = s[i:]
            for word in words:
                if target.startswith(word):
                    for j in range(i+len(word), n+1):
                        dp[j] = min(dp[j], dp[i]-len(word))

        return dp[-1]
