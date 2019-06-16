class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def check_row(r):
            counter = [0] * 10
            for val in r:
                if val != '.':
                    val = int(val)
                    counter[val] += 1
                    if counter[val] > 1:
                        return False
            return True

        for row in board:
            if not check_row(row):
                return False

        for ci in range(9):
            col = [board[i][ci] for i in range(9)]
            if not check_row(col):
                return False

        blocks = []
        # Don't use [[]] * 9
        for _ in range(9):
            blocks.append([])

        for ri in range(9):
            for ci in range(9):
                bid = ci/3*3 + ri/3
                blocks[bid].append(board[ci][ri])

        for block in blocks:
            if not check_row(block):
                return False

        return True

input = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

s = Solution()
print s.isValidSudoku(input)

