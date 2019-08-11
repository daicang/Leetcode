class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []

        for part in path.split('/'):
            if part == '':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            elif part == '.':
                continue
            else:
                stack.append(part)

        return '/%s' % '/'.join(stack)
