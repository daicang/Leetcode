class Solution(object):
    def largestRectangleArea1(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        # Divide and conquer

        size = len(heights)
        if not heights:
            return 0
        if size == 1:
            return heights[0]

        min_idx = 0
        minimal = heights[0]
        for idx, val in enumerate(heights):
            if val < minimal:
                minimal = val
                min_idx = idx

        return max([size*minimal, self.largestRectangleArea(heights[:min_idx]), self.largestRectangleArea(heights[:min_idx+1])])

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = [-1]

        for idx, h in enumerate(heights):
            if stack[-1] != -1 and h < heights[stack[-1]]:
                while stack[-1] != -1 and heights[stack[-1]] >= h:
                    curr = stack.pop()
                    max_area = max(max_area, heights[curr] * ((idx-1)-(stack[-1]+1)+1))

            stack.append(idx)

        while stack[-1] != -1:
            curr = stack.pop()
            max_area = max(max_area, heights[curr] * (len(heights)-stack[-1]-1))

        return max_area
