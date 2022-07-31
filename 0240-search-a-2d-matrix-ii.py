from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def search(r_start, r_end, c_start, c_end):

            if r_end < r_start or c_end < c_start:
                return False
            if r_start == r_end:
                l = c_end - c_start + 1
                if l < 5:
                    # Linear search
                    for i in range(c_start, c_end+1):
                        if matrix[r_start][i] == target:
                            return True
                    return False
                else:
                    # Binary search
                    mid = (c_start + c_end) // 2
                    return search(r_start, r_end, c_start, mid) or search(r_start, r_end, mid+1, c_end)

            if c_start == c_end:
                l = r_start - r_end + 1
                if l < 5:
                    for i in range(r_start, r_end+1):
                        if matrix[i][c_start] == target:
                            return True
                    return False
                else:
                    mid = (r_start + r_end) // 2
                    return search(r_start, mid, c_start, c_end) or search(mid+1, r_end, c_start, c_end)

            r_mid = r_start + (r_end - r_start) // 2
            c_mid = c_start + (c_end - c_start) // 2
            pivot = matrix[r_mid][c_mid]

            if pivot == target:
                return True

            if pivot < target:
                return search(r_mid+1, r_end, c_mid+1, c_end) or search(r_start, r_mid, c_mid+1, c_end) or search(r_mid+1, r_end, c_start, c_mid)
            else:
                return search(r_start, r_mid-1, c_start, c_mid-1) or search(r_start, r_mid-1, c_mid, c_end) or search(r_mid, r_end, c_start, c_mid-1)

        m = len(matrix)
        if m == 0:
            return False

        n = len(matrix[0])
        if n == 0:
            return False

        return search(0, m-1, 0, n-1)

s = Solution()

inputs = [
    [[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20],
    [[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 0],
]

for i in inputs:
    print(s.searchMatrix(*i))
