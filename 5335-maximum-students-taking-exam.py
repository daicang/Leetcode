from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        rows = len(seats)
        cols = len(seats[0])

        def compatible(row1, row2):
            if (row2<<1) & row1:
                return False
            if (row2>>1) & row1:
                return False
            return True

        def count_mask(mask):
            count = 0
            while mask > 0:
                count += mask & 1
                mask >>= 1
            return count

        students = []
        seat_masks = []
        for row in range(rows):
            seat_mask = 0
            for seat in seats[row]:
                seat_mask <<= 1
                if seat == '#':
                    seat_mask += 1
            seat_masks.append(seat_mask)
            students.append([0]*(1<<cols))

        for row in range(rows):
            for mask in range(1<<cols):
                if mask & seat_masks[row]:
                    continue

                # Check neighboring
                if mask & (mask<<1):
                    continue

                if row == 0:
                    students[0][mask] = count_mask(mask)
                else:
                    for last_mask in range(1<<cols):
                        if compatible(last_mask, mask):
                            students[row][mask] = max(students[row][mask], students[row-1][last_mask]+count_mask(mask))

        return max(*students[rows-1])

s = Solution()

data = [
    [
        ["#",".","#","#",".","#"],
        [".","#","#","#","#","."],
        ["#",".","#","#",".","#"]
    ],  # 4

    [
        [".","#"],
        ["#","#"],
        ["#","."],
        ["#","#"],
        [".","#"]
    ],  # 3

    [
        ["#",".",".",".","#"],
        [".","#",".","#","."],
        [".",".","#",".","."],
        [".","#",".","#","."],
        ["#",".",".",".","#"]
    ], # 10

    [[".",".",".",".","#",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".","#","."],
    [".",".",".",".",".",".",".","."],
    [".",".","#",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".","#",".",".","#","."]],
]

for d in data:
    print(s.maxStudents(d))