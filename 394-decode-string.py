class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def _find_digit(s):
            for i, ch in enumerate(s):
                if ch.isdigit():
                    return i
            return False

        def _find_right_paren(s):
            counter = 0
            for i, ch in enumerate(s):
                if ch == '[':
                    counter += 1
                if ch == ']':
                    counter -= 1
                    if counter == 0:
                        return i
            return False

        def _parse(s):
            if not s:
                return ''
            if s[0].isalpha():
                next = _find_digit(s)
                if next:
                    return s[:next] + _parse(s[next:])
                return s
            else:
                left_paren = s.find('[')
                right_paren = _find_right_paren(s)
                num = int(s[:left_paren])
                return num * _parse(s[left_paren+1:right_paren]) + _parse(s[right_paren+1:])

        return _parse(s)

s = Solution()
print s.decodeString('3[a2[c]]')
print s.decodeString('2[a]3[c]4[b]5[d]')
