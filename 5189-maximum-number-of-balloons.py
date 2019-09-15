class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counter = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        flags = {
            'l': False,
            'o': False
        }

        for ch in text:
            if ch not in counter:
                continue
            if ch in flags:
                if not flags[ch]:
                    flags[ch] = True
                    continue
                else:
                    flags[ch] = False
            counter[ch] += 1

        return min(counter.values())

s = Solution()

inputs = [
    "loonbalxballpoon",
    'leetcode'
]

for i in inputs:
    print s.maxNumberOfBalloons(i)
