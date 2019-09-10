class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        if rowIndex == 0:
            return []

        last_row = [1]

        for i in range(1, rowIndex):
            row = [1]
            for j in range(1, i):
                row.append(last_row[j-1]+last_row[j])
            row.append(1)
            last_row = row

        return last_row

s = Solution()

print s.getRow(2)
print s.getRow(3)

