class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def check(r):
            counter = [0] * 10
            for val in r:
                if val != '.':
                    val = int(val)
                    counter[val] += 1
                    if counter[val] > 1:
                        return False
            return True

        rows = board
        cols = [[board[r][c] for r in range(9)] for c in range(9)]
        blocks = []
        for _ in range(9):
            blocks.append([])
        for ri in range(9):
            for ci in range(9):
                bid = ci/3*3 + ri/3
                blocks[bid].append(board[ri][ci])

        slots = []
        r, c = 0, 0
        while r < 9:
            if board[r][c] == '.':
                slots.append((r, c))
            c += 1
            if c > 8:
                c = 0
                r += 1

        def set_val(r, c, val, check=False):
            '''
            Check: check collision when [r,c] set to val
            '''
            block_idx = c/3*3 + r/3
            if check:
                if (val in rows[r]) or (val in cols[c]) or (val in blocks[block_idx]):
                    return False
            rows[r][c] = str(val)
            cols[c][r] = str(val)
            block_inner_idx = c%3*3 + r%3
            blocks[block_idx][block_inner_idx] = val
            return True

        def backtrack(slot_idx):
            '''
            slot_idx is index of slot to fill,
            return True if found solution, False if no solution
            '''
            if slot_idx == len(slots):
                # All numbers filled
                return True

            r, c = slots[slot_idx]
            for val in range(1, 10):
                if set_val(r, c, str(val), check=True):
                    # Set [r,c]=val, proceed next slot
                    if backtrack(slot_idx+1):
                        # Found the answer
                        return True
            # No available fill, restore [r,c]
            set_val(r, c, '.')
            return False

        backtrack(0)

input = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
s = Solution()
s.solveSudoku(input)

for line in input:
    print line

