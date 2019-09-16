class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []

        from collections import defaultdict

        ladders = []
        mapper = defaultdict(list)
        neighbors = defaultdict(set)

        def keys(word):
            keys = []
            for i in range(len(word)):
                keys.append(word[:i] + '*' + word[i+1:])
            return keys

        for word in wordList:
            for key in keys(word):
                mapper[key].append(word)

        def bfs():
            queue = [beginWord]
            end = False
            level = 0

            while queue and not end:
                level += 1
                size = len(queue)

                for i in range(size):
                    word = queue[i]

                    if word == endWord:
                        end = True

                    for key in keys(word):
                        for next_ in mapper[key]:
                            queue.append(next_)
                            neighbors[word].add(next_)

            return level

        path_length = bfs()
        # print neighbors

        def backtrack(word, path, visited_keys, level):
            if level > path_length:
                return

            if word == endWord:
                # print level
                ladders.append(path+[])
                return

            for next_ in neighbors[word]:
                path.append(next_)
                backtrack(next_, path, visited_keys, level+1)
                path.pop()

        backtrack(beginWord, [beginWord,], [], 1)

        return ladders


s = Solution()

inpus = [
    ["hit", "cog", ["hot","dot","dog","lot","log","cog"]],
    ["red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]],
    ["cat", "fin", ["ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","fin","bug","can","hes","col","pep","tug","ump","arc","fee","lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe","pis","dot","jaw","hat","roe","ada","mac"]]
]

for i in inpus:
    print(s.findLadders(*i))
