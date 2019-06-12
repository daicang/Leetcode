class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        val = 0
        for i, char in enumerate(s):
            v = values[char]
            if i != len(s)-1:
                if v < values[s[i+1]]:
                    v *= -1
            val += v
        return val
