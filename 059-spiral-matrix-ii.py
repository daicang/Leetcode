class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        array = []
        for _ in range(n):
            array.append([None] * n)

        start = 0
        end = n-1
        i = 1

        while start < end:
            for col in range(start, end):
                array[start][col] = i
                i += 1
            for row in range(start, end):
                array[row][end] = i
                i += 1
            for col in range(end, start, -1):
                array[end][col] = i
                i += 1
            for row in range(end, start, -1):
                array[row][start] = i
                i += 1

            start += 1
            end -= 1

        if start == end:
            array[start][start] = i

        return array