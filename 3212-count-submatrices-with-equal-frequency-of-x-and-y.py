class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        # time: O(rows*cols)
        # space: O(cols)
        count = 0
        rows, cols = len(grid), len(grid[0])
        # buffer holds count_x, count_y for up to [row-1][col]
        buffer = [[0, 0]] * cols

        for row in range(rows):
            # row_buffer holds count_x, count_y for current row
            row_buffer = [0, 0]
            for col in range(cols):
                val = grid[row][col]
                if val == 'X':
                    row_buffer[0] += 1
                elif val == 'Y':
                    row_buffer[1] += 1
                if row == 0:
                    buffer[col] = [row_buffer[0], row_buffer[1]]
                else:
                    # count = buffer + row_buffer
                    buffer[col][0] += row_buffer[0]
                    buffer[col][1] += row_buffer[1]
                if buffer[col][0] != 0 and buffer[col][0] == buffer[col][1]:
                    count += 1

        return count
