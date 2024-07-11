
from typing import List

large_n = 10**10

class Node:
    def __init__(self):
        self.children = {}
        self.cost = large_n


class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word, cost):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.cost = min(node.cost, cost)

    def match(self, s, start):
        # match from s[start]
        # return list of [next_start_index, cost]
        node = self.root
        results = []
        for i in range(start, len(s)):
            ch = s[i]
            if ch not in node.children:
                break
            node = node.children[ch]
            if node.cost < large_n:
                results.append([i+1, node.cost])
        return results


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        # trie + dp(0-1 backpack)
        # time: O(len(target)*avg_len(words[i]))
        # space: O(len(target)+len(words))
        tr = Trie()
        for word, cost in zip(words, costs):
            tr.add_word(word, cost)

        # cost on matching [0, i-1]
        dp = [large_n] * (len(target) + 1)
        dp[0] = 0

        for i in range(len(target)):
            if dp[i] == large_n:
                continue
            results = tr.match(target, i)
            for idx, cost in results:
                dp[idx] = min(dp[idx], dp[i]+cost)

        return -1 if dp[-1] == large_n else dp[-1]


inputs = [
    ["ababababab", ["ab","abab","babab"], [2,2,5]],
    ["zqkvhwwemqdfpopxvasayaaergirzwlwhh", ["g","a","emqdfpopxvasa","hw","wwemqd","lwhh","i","z","zqkvhwwemqdfpopxvasayaaergirzw","lw","z","sayaaergirzwlwh","vasayaaerg","zqkvhwwemqdfpopxvasayaaergir","kvhwwemqdfpopxvasayaaergi","h","mqdfpopxvasayaaergirzw","fpop"], [75,23,59,87,17,87,53,55,21,93,67,69,21,10,18,46,82,21]],
]

s = Solution()

for i in inputs:
    print(s.minimumCost(*i))
