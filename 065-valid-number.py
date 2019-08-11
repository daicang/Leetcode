class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()

        if not s:
            return False

        def valid_int(i):
            for ch in i:
                if ch not in '0123456789':
                    return False
            return True

        def valid_float(p):
            if not p:
                return False
            if p[0] in '-+':
                p = p[1:]
            if not p or p == '.':
                return False

            parts = p.split('.')
            if len(parts) not in (1, 2):
                return False

            if not valid_int(parts[0]):
                print '%s p0 invalid' % parts[0]
                return False

            if len(parts) == 2 and not valid_int(parts[1]):
                print '%s p1 invalid' % parts[1]
                return False

            return True

        parts = s.split('e')
        if len(parts) not in (1, 2):
            return False

        if not valid_float(parts[0]):
            return False

        if len(parts) == 2:
            if '.' in parts[1]:
                return False
            if not valid_float(parts[1]):
                return False

        return True


s = Solution()
inputs = [
    '0', # t
    '6e6.5', # f
    '0e', # f
    "005047e+6", # t
]

for input in inputs:
    print s.isNumber(input)


