class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        from collections import deque
        x = abs(x)
        y = abs(y)

        visited = set()
        directions = [[1, 2], [2, 1], [-1, 2], [1, -2], [-2, 1], [2, -1], [-1, -2], [-2, -1]]

        # coordinate and distance
        queue = deque([[0, 0, 0]])

        # bfs
        while queue:
            a, b, dist = queue.popleft()

            if (a, b) == (x, y):
                return dist

            if (a, b) in visited:
                continue

            visited.add((a, b))
            moves = [(a+move[0], b+move[1]) for move in directions]
            moves.sort(key=lambda p: abs(x-p[0])+abs(y-p[1]))

            # if we move all 6(or 8) directions, TLE
            for move in moves[:2]:
                a1 = move[0]
                b1 = move[1]
                if (a1, b1) not in visited:
                    queue.append([a1, b1, dist+1])

s = Solution()

inputs = [
    (2, 1),
    (5, 5),  # 4
    (2, 112), # 56
]

for i in inputs:
    print s.minKnightMoves(*i)
