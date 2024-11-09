class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        minval = inf

        for n in nums:
            while stack and stack[-1][0] <= n:
                stack.pop()
            if stack and stack[-1][1] < n:
                return True
            minval = min(minval, n)
            stack.append((n, minval))

        return False
