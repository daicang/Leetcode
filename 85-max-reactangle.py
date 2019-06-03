# *
class Solution(object):

    # DP
    def maximalRectangle_dp(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        height = [0] * cols

        left = [-1] * cols
        right = [cols] * cols

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == '1':
                    height[col] = height[col] + 1
                else:
                    height[col] = 0

            last_col = -1
            # expand left, index of first zero element
            for col in range(cols):
                if matrix[row][col] == '1':
                    left[col] = max(left[col], last_col)
                else:
                    left[col] = -1  # for 'max' for next row
                    last_col = col

            last_col = cols
            # expand right, index of fist zero element
            for col in range(cols-1, -1, -1):
                if matrix[row][col] == '1':
                    right[col] = min(right[col], last_col)
                else:
                    right[col] = cols
                    last_col = col

            for col in range(cols):
                # print height[col], right[col], left[col]
                max_area = max(max_area, height[col] * (right[col] - left[col] - 1))

            print(matrix[row])
            print(height)
            print(left)
            print(right)
            print('\n')

        return max_area



    # Histogram with stack
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])

        # Solve histogram
        def max_hist(l):
            max_area = 0
            stack = [-1]

            for r_i, h in enumerate(l):
                if stack[-1] != -1 and h < l[stack[-1]]:
                    while stack[-1] != -1 and l[stack[-1]] > h:
                        curr = stack.pop()
                        max_area = max(max_area, l[curr] * (r_i - stack[-1] - 1))
                stack.append(r_i)

            while stack[-1] != -1:
                curr = stack.pop()
                max_area = max(max_area, l[curr] * (len(l) - stack[-1] - 1))

            return max_area

        maxrec = 0

        # Convert to histogram
        h = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    h[j] = h[j] + 1
                else:
                    h[j] = 0

            maxrec = max(maxrec, max_hist(h))

        return maxrec


s = Solution()
print(s.maximalRectangle([['1']]))
print(s.maximalRectangle([["1","0","1","0","0"],
                          ["1","0","1","1","1"],
                          ["1","1","1","1","1"],
                          ["1","0","0","1","0"]]))

print(s.maximalRectangle([['0', '0', '0'],
                          ['0', '0', '0'],
                          ['1', '1', '1']]))
