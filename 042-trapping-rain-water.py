class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        total = 0
        size = len(height)
        maxleft = [0] * size
        maxright = [0] * size

        for i in range(1, size):
            maxleft[i] = max(maxleft[i-1], height[i-1])

        for i in range(size-2, -1, -1):
            maxright[i] = max(maxright[i+1], height[i+1])

        for i in range(size):
            h = min(maxleft[i], maxright[i])
            if h > height[i]:
                total += h - height[i]

        return total


s = Solution()
inputs = [
    [0,1,0,2,1,0,1,3,2,1,2,1],  # 6
]

for input in inputs:
    print(s.trap(input))
