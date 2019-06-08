class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []

        pop_i = 0
        for p in pushed:
            stack.append(p)
            while stack and pop_i < len(popped) and stack[-1] == popped[pop_i]:
                stack.pop()
                pop_i += 1

        if stack or pop_i != len(popped):
            return False
        return True


s = Solution()

print(s.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))

print(s.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
