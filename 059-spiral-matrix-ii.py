from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = []
        for _ in range(n):
            arr.append([None] * n)

        start = 0
        end = n-1
        val = 1

        while start < end:
            for i in range(start, end+1):
                arr[start][i] = val
                val += 1

            for i in range(start+1, end+1):
                arr[i][end] = val
                val += 1

            for i in range(end-1, start-1, -1):
                arr[end][i] = val
                val += 1

            for i in range(end-1, start, -1):
                arr[i][start] = val
                val += 1

            start += 1
            end -= 1

        if start == end:
            arr[start][end] = val

        return arr
