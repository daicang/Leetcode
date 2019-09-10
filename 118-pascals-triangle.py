class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        result = [[1]]
        for n in range(1, numRows):
            row = [1]
            last_row = result[n-1]
            for i in range(1, n):
                row.append(last_row[i-1]+last_row[i])
            row.append(1)
            result.append(row)

        return result
