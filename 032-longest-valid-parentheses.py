class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_counter = 0
        lefts = [0] * len(s)
        dp = [0] * len(s)
        maxlen = 0

        for i, ch in enumerate(s):
            if ch == '(':
                left_counter += 1
            else:
                # Right parenthese
                left_counter -= 1
            lefts[i] = left_counter

        for i, l in enumerate(lefts):
            if i > 0 and lefts[i] > lefts[i-1]:
                continue
            for j in range(i-1, -1, -1):
                if lefts[j] == l:
                    dp[i] = (i-j) + dp[j]
                    break
            else:
                if l == 0:
                    dp[i] = i+1
            maxlen = max(maxlen, dp[i])

        return maxlen


inputs = [
    "()",  # 2
    ")()())",  # 4
    "()(())",  # 6
]

s = Solution()

for input in inputs:
    print input, s.longestValidParentheses(input)

