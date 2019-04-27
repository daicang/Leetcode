# coding: utf-8

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0

        for idx, row in enumerate(board):
            if 'R' in row:
                rindex = idx
                break

        for idx, element in enumerate(row):
            if element == 'R':
                cindex = idx
                break

        def find_in_row(row, index):
            # print row
            ret = 0
            # print row[index+1:]
            for element in row[index+1:]:
                if element.isupper():
                    break
                elif element.islower():
                    ret += 1
                    break

            # print row[:index:-1]
            for element in row[:index][::-1]:
                if element.isupper():
                    break
                elif element.islower():
                    ret += 1
                    break
            return ret

        count += find_in_row(board[rindex], cindex)
        col = []
        for row in board:
            col.append(row[cindex])

        count += find_in_row(col, rindex)
        return count

s = Solution()
print(s.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))