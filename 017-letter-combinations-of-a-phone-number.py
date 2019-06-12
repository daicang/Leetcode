class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        itoch = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        last = []
        curr = []

        for ch in itoch[digits[0]]:
            last.append(ch)

        for d in digits[1:]:
            for ch in itoch[d]:
                for s in last:
                    curr.append(s+ch)
            last = curr
            curr = []

        return last



s = Solution()
print(s.letterCombinations('7'))
