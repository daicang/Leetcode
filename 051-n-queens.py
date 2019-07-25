
def print_arr(arr):
    for row in arr:
        print ' '.join(['{:>2}'.format(ch) for ch in row])
    print '\n'


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        board = []
        for _ in range(n):
            board.append(['.'] * n)

        results = []

        cols = [0] * n
        s1 = [0] * (n+n)
        s2 = {key: 0 for key in range(-n, n)}

        def traceback(row):
            if row == n:
                results.append([''.join(row) for row in board])
                return

            for col in range(n):
                s = row+col
                d = row-col
                if cols[col] == 1 or s1[s] == 1 or s2[d] == 1:
                    continue

                cols[col] = 1
                s1[s] = 1
                s2[d] = 1
                board[row][col] = 'Q'
                # print 'set %s,%s' % (row, col)

                # print_arr(board)
                traceback(row+1)

                cols[col] = 0
                s1[s] = 0
                s2[d] = 0
                # print 'revert %s,%s' % (row, col)
                board[row][col] = '.'

        traceback(0)

        return results

s = Solution()

result = s.solveNQueens(4)

for arr in result:
    print_arr(arr)



