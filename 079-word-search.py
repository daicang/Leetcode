class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board or not board[0]:
            return False

        rows = len(board)
        cols = len(board[0])

        used = []
        for _ in range(rows):
            used.append([False] * cols)

        def search_around(row, col, char):
            if row < rows-1 and not used[row+1][col] and board[row+1][col] == char:
                yield row+1, col
            if col < cols-1 and not used[row][col+1] and board[row][col+1] == char:
                yield row, col+1
            if row > 0 and not used[row-1][col] and board[row-1][col] == char:
                yield row-1, col
            if col > 0 and not used[row][col-1] and board[row][col-1] == char:
                yield row, col-1

        def bt(i, last_row, last_col):
            if i == len(word):
                # All word matches
                return True

            for row, col in search_around(last_row, last_col, word[i]):
                used[row][col] = True
                if bt(i+1, row, col):
                    return True
                used[row][col] = False

            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    used[row][col] = True
                    if bt(1, row, col) is True:
                        return True
                    used[row][col] = False

        return False

s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
words = [
    "ABCCED",
    'SEE',
    'ABCB'
]

for word in words:
    print s.exist(board, word)

print s.exist([['a', 'a']], 'aaa')


