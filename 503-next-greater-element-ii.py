class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # monotonic stack
        nums = nums[::-1]
        stack = nums[:]  # must copy!
        greaters = []  # previous greater element

        for val in nums:
            while stack and stack[-1] <= val:
                stack.pop()
            if stack:
                greaters.append(stack[-1])
            else:
                greaters.append(-1)
            stack.append(val)
        return greaters[::-1]