class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows = len(mat)
        cols = len(mat[0])
        visited = set()

        def encode(matrix):
            val = 0
            for row in matrix:
                for elem in row:
                    val <<= 1
                    if elem == 1:
                        val += 1
            return val

        def flip(m, r, c):
            m[r][c] ^= 1
            for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r1 = r + delta[0]
                c1 = c + delta[1]
                if 0 <= r1 < rows and 0 <= c1 < cols:
                    m[r1][c1] ^= 1

        def all_zero(m):
            for row in m:
                for ele in row:
                    if ele == 1:
                        return False
            return True

        import copy
        import heapq
        h = [(0, mat)]
        visited.add(encode(mat))

        # bfs
        while h:
            count, matrix = heapq.heappop(h)
            if all_zero(matrix):
                return count

            count += 1
            for row in range(rows):
                for col in range(cols):
                    m1 = copy.deepcopy(matrix)
                    flip(m1, row, col)

                    encoded = encode(m1)
                    if encoded in visited:
                        continue
                    visited.add(encoded)
                    heapq.heappush(h, (count, m1))

        return -1

s = Solution()

data = [
    [[0,0],[0,1]],
    [[1,1,1],[1,0,1],[0,0,0]],
    [[1,0,0],[1,0,0]],
    [[0]]
]

for d in data:
    print s.minFlips(d)

