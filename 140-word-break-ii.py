class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        import copy
        if not wordDict:
            return []

        cache = {}

        def search(begin):
            if begin in cache:
                return cache[begin]

            if begin == len(s):
                return [['']]

            res = []
            for end in range(begin, len(s)):
                word = s[begin:end+1]
                if word in wordDict:
                    for wlist in search(end+1):
                        wlist = copy.copy(wlist)
                        wlist.insert(0, word)
                        res.append(wlist)

            cache[begin] = res
            return res

        search(0)
        results = []
        for r in cache[0]:
            results.append(' '.join(r).strip())

        return results

s = Solution()

data = [
    ["catsanddog", ["cat", "cats", "and", "sand", "dog"]],
    ["pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]],
    ["catsandog", ["cats", "dog", "sand", "and", "cat"]],
    ['a', ['a']]
]

for d in data:
    print s.wordBreak(*d)
