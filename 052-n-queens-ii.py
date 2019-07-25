class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0]
        cols = [0] * n
        s1 = [0] * (n+n)
        s2 = {key: 0 for key in range(-n, n)}

        def traceback(row):
            if row == n:
                count[0] += 1
                return

            for col in range(n):
                s = row+col
                d = row-col
                if cols[col] == 1 or s1[s] == 1 or s2[d] == 1:
                    continue

                cols[col] = 1
                s1[s] = 1
                s2[d] = 1

                traceback(row+1)

                cols[col] = 0
                s1[s] = 0
                s2[d] = 0

        traceback(0)

        return count[0]