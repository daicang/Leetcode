class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # consider matrix as list of column vectors
        def compress(mat):
            # compress as list of column vectors
            rows, cols = len(mat), len(mat[0])
            compressed = []
            for _ in range(cols):
                compressed.append([])
            for c in range(cols):
                for r in range(rows):
                    if mat[r][c]:
                        compressed[c].append([r, mat[r][c]])
            return compressed

        cm1 = compress(mat1)
        cm2 = compress(mat2)

        rows1 = len(mat1)
        cols2 = len(mat2[0])

        ans = []
        for _ in range(rows1):
            ans.append([0] * cols2)

        for c in range(cols2):
            vec2 = cm2[c]
            for c1, val2 in vec2:
                # mat1[col1] *= val2
                for r, val1 in cm1[c1]:
                    ans[r][c] += val1 * val2

        return ans

    def multiply_row(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def compress(mat):
            rows, cols = len(mat), len(mat[0])
            compressed = []
            for _ in range(rows):
                compressed.append([])
            for r in range(rows):
                for c in range(cols):
                    if mat[r][c]:
                        compressed[r].append([c, mat[r][c]])
            return compressed

        cm1 = compress(mat1)
        cm2 = compress(mat2)

        rows1 = len(mat1)
        cols2 = len(mat2[0])

        ans = []
        for _ in range(rows1):
            ans.append([0] * cols2)

        for r1 in range(rows1):
            for c1, val1 in cm1[r1]:
                for c2, val2 in cm2[c1]:
                    ans[r1][c2] += val1 * val2

        return ans
