from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [None] * (len(s)+1)

        def bfs(start):
            if start == len(s):
                return True
            substr = s[start:]
            for word in wordDict:
                if substr.startswith(word):
                    if memo[start+len(word)] is False:
                        continue
                    if bfs(start+len(word)):
                        return True
            memo[start] = False
            return False

        return bfs(0)

s = Solution()

data = [
    ['leetcode', ["leet", "code"]],
    ["applepenapple", ["apple", "pen"]],
    ["catsandog", ["cats", "dog", "sand", "and", "cat"]],
    ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
     ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]]
]

for d in data:
    print(s.wordBreak(*d))

