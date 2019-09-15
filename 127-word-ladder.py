class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        def has_edge(w1, w2):
            flag = 0
            for i, ch1 in enumerate(w1):
                ch2 = w2[i]
                if ch1 != ch2:
                    if flag == 0:
                        flag = 1
                    else:
                        return False
            return True

        queue = [beginWord]

        def bfs():




