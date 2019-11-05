class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = 0
        right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1

        result = set()

        def recurse(index, left_rem, right_rem, left_count, right_count, expr):
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    result.add(''.join(expr))
                return

            if s[index] == '(':
                if left_rem > 0:
                    # discard this left parenthesis
                    recurse(index+1, left_rem-1, right_rem, left_count, right_count, expr)

                recurse(index+1, left_rem, right_rem, left_count+1, right_count, expr+['('])

            elif s[index] == ')':
                if right_rem > 0:
                    # discard this right parenthesis
                    recurse(index+1, left_rem, right_rem-1, left_count, right_count, expr)

                if left_count > right_count:
                    recurse(index+1, left_rem, right_rem, left_count, right_count+1, expr+[')'])

            else:
                recurse(index+1, left_rem, right_rem, left_count, right_count, expr+[s[index]])

        recurse(0, left, right, 0, 0, [])

        return list(result)


s = Solution()

inputs = [
    "()())()",
    "(a)())()",
    ')(',
]

for i in inputs:
    print s.removeInvalidParentheses(i)
