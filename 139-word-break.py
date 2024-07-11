from typing import List

class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.is_end = True

    def search(self, s, i):
        # return next search index
        matches = []
        node = self.root

        while i < len(s):
            ch = s[i]
            if ch not in node.children:
                break
            else:
                node = node.children[ch]
                if node.is_end:
                    matches.append(i+1)
                i += 1
        return matches


class Solution:
    def wordBreak_bfs(self, s: str, wordDict: List[str]) -> bool:
        # BFS with dp
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

    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:
        # dp with starting index
        words = set(wordDict)
        dp = [False] * (len(s)+1)

        for i in range(len(s)+1):
            if i == 0 or dp[i]:
                target = s[i:]
                for word in words:
                    if target.startswith(word):
                        next_i = i + len(word)
                        if next_i == len(s):
                            return True
                        dp[next_i] = True

        return False

    def wordBreak_trie(self, s: str, wordDict: List[str]) -> bool:
        # trie with dp
        tr = Trie()
        for word in wordDict:
            tr.add_word(word)

        dp = [False] * (len(s)+1)
        for i in range(len(s)+1):
            if i == 0 or dp[i]:
                for j in tr.search(s, i):
                    dp[j] = True
                    if j == len(s):
                        return True
        return False
