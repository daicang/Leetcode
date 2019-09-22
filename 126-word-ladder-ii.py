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

        wordList = set(wordList)
        layer = {}
        layer[beginWord] = [[beginWord]]
        ladders = []

        while layer:
            next_layer = defaultdict(list)
            for w in layer:
                if w == endWord:
                    for l in layer[w]:
                        ladders.append(l)
                else:
                    for i in range(len(w)):
                        for ch in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = ''.join([w[:i], ch, w[i+1:]])
                            if new_word in wordList:
                                next_layer[new_word] += [c+[new_word] for c in layer[w]]

            wordList -= set(next_layer.keys())
            layer = next_layer

        return ladders


s = Solution()

inpus = [
    ["hit", "cog", ["hot","dot","dog","lot","log","cog"]],
    ["red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]],
    ["cat", "fin", ["ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","fin","bug","can","hes","col","pep","tug","ump","arc","fee","lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe","pis","dot","jaw","hat","roe","ada","mac"]]
]

for i in inpus:
    print(s.findLadders(*i))
