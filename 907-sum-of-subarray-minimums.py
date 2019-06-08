class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)

        stack = []
        prev_smaller = [None] * length
        for i in range(length):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        next_smaller = [None] * length
        for i in range(length-1, -1, -1):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            next_smaller[i] = stack[-1] if stack else length
            stack.append(i)

        # print('input: %s' % A)
        # print('prev-small: %s' % prev_smaller)
        # print('next-small: %s' % next_smaller)

        return sum([(i-prev_smaller[i]) * (next_smaller[i]-i) * A[i] for i in range(length)]) % (10**9 + 7)

s = Solution()
print(s.sumSubarrayMins([3,1,2,4]))
