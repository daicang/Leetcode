class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        from collections import defaultdict

        mapper = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                mapper[key].append(word)

        queue = [beginWord]
        level = 0

        while queue:
            neighbors = []
            level += 1

            for curr in queue:
                if curr == endWord:
                    return level

                for i in range(len(curr)):
                    key = curr[:i] + '*' + curr[i+1:]
                    if key in mapper:
                        neighbors.extend(mapper[key])
                        del mapper[key]

            queue = neighbors

        return 0


s = Solution()
inputs = [
    ['hit', 'cog', ["hot","dot","dog","lot","log","cog"]],
    ["hit", "cog", ["hot","dot","dog","lot","log"]],
    ['a', 'c', ['a', 'b', 'c']]
]

for i in inputs:
    print s.ladderLength(*i)

