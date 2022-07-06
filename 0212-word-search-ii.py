from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        from collections import defaultdict
        char_map = defaultdict(list)

        if len(board) == 0 or len(board[0]) == 0:
            return []

        rows = len(board)
        cols = len(board[0])

        def reset_trace(trace):
            for row in trace:
                for c in range(len(row)):
                    row[c] = False

        for row, r in enumerate(board):
            for col, ch in enumerate(r):
                char_map[ch].append((row, col))

        found = []
        trace = []
        for _ in range(rows):
            trace.append([False] * cols)

        def explore(word, idx, row, col, trace):
            if board[row][col] != word[idx]:
                return False

            if idx == len(word)-1:
                return True

            for next_pos in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                next_row, next_col = next_pos
                if next_row < 0 or next_col < 0 or next_row >= rows or next_col >= cols:
                    continue
                if trace[next_row][next_col]:
                    continue
                trace[next_row][next_col] = True
                if explore(word, idx+1, next_row, next_col, trace):
                    return True
                trace[next_row][next_col] = False

        for word in words:
            if len(word) == 0:
                found.append(word)
                continue

            reset_trace(trace)

            for pos in char_map[word[0]]:
                row, col = pos
                trace[row][col] = True
                if explore(word, 0, row, col, trace):
                    found.append(word)
                    break
                trace[row][col] = False

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