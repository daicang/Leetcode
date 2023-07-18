from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = []
        arr = nums[::-1]
        stack = nums[::-1]
        for n in arr:
            while stack and stack[-1] <= n:
                stack.pop()
            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)
            stack.append(n)

        return result[::-1]
