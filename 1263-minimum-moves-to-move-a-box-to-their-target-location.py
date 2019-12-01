class Solution(object):
    def minPushBox(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        import heapq

        rows = len(grid)
        cols = len(grid[0])

        for rid, row in enumerate(grid):
            for cid, val in enumerate(row):
                if val == 'S':
                    player = [rid, cid]
                elif val == 'B':
                    box = [rid, cid]
                elif val == 'T':
                    target = [rid, cid]

        def get_weight(b0, b1, moves):
            return (moves, abs(b0 - target[0]) + abs(b1 + target[1]))

        def moves_from_weight(w):
            return w[0]

        visited = set()

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols and grid[x][y] != '#'

        h = []
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
        heapq.heappush(h, (get_weight(box[0], box[1], 0), (box[0], box[1], player[0], player[1])))

        while h:
            weight, position = heapq.heappop(h)
            if position in visited:
                continue

            moves = moves_from_weight(weight)
            visited.add(position)
            b0, b1, p0, p1 = position

            for direction in directions:
                p0_new = p0 + direction[0]
                p1_new = p1 + direction[1]
                if is_valid(p0_new, p1_new):
                    if p0_new == b0 and p1_new == b1:
                        b0_new = b0 + direction[0]
                        b1_new = b1 + direction[1]

                        if b0_new == target[0] and b1_new == target[1]:
                            return moves+1

                        if is_valid(b0_new, b1_new):
                            heapq.heappush(h, (get_weight(b0_new, b1_new, moves+1), (b0_new, b1_new, p0_new, p1_new)))
                    else:
                        heapq.heappush(h, (get_weight(b0, b1, moves), (b0, b1, p0_new, p1_new)))

        return -1


s = Solution()

data = [
    [["#","#","#","#","#","#"],
    ["#","T","#","#","#","#"],
    ["#",".",".","B",".","#"],
    ["#",".","#","#",".","#"],
    ["#",".",".",".","S","#"],
    ["#","#","#","#","#","#"]],

    [["#","#","#","#","#","#"],
    ["#","T","#","#","#","#"],
    ["#",".",".","B",".","#"],
    ["#","#","#","#",".","#"],
    ["#",".",".",".","S","#"],
    ["#","#","#","#","#","#"]],

    [["#","#","#","#","#","#"],
    ["#","T",".",".","#","#"],
    ["#",".","#","B",".","#"],
    ["#",".",".",".",".","#"],
    ["#",".",".",".","S","#"],
    ["#","#","#","#","#","#"]],

    [["#","#","#","#","#","#","#"],
    ["#","S","#",".","B","T","#"],
    ["#","#","#","#","#","#","#"]],

    [["#",".",".","#","#","#","#","#"],
    ["#",".",".","T","#",".",".","#"],
    ["#",".",".",".","#","B",".","#"],
    ["#",".",".",".",".",".",".","#"],
    ["#",".",".",".","#",".","S","#"],
    ["#",".",".","#","#","#","#","#"]]
]

for d in data:
    print s.minPushBox(d)

