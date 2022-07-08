from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        from collections import defaultdict
        char_map = defaultdict(list)

        if len(board) == 0 or len(board[0]) == 0:
            return []

        rows = len(board)
        cols = len(board[0])

        found = []
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = word

        def backtrack(row, col, parent):
            ch = board[row][col]
            node = parent[ch]
            if node.get('#'):
                found.append(node['#'])
                del node['#']

            board[row][col] = '#'

            for next_row, next_col in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                if next_row < 0 or next_col < 0 or next_row >= rows or next_col >= cols:
                    continue
                next_char = board[next_row][next_col]
                if node.get(next_char):
                    backtrack(next_row, next_col, node)

            board[row][col] = ch

        for row in range(rows):
            for col in range(cols):
                ch = board[row][col]
                if trie.get(ch):
                    backtrack(row, col, trie)

        return found



s = Solution()

inputs = [
    [[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]],
    [[["a","b"],["c","d"]], ["abcb"]],
    [[["a","a"]], ["aaa"]],
    [[['a']], ['a']]
]

for i in inputs:
    print(s.findWords(*i))