class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeats = set()

        if len(s) <= 10:
            return []

        h_map = {'A': 0, 'T': 1, 'G': 2, 'C': 3}

        h = 0
        shift = 1 << 20
        for start in range(len(s)-9):
            if start == 0:
                for i in range(10):
                    h <<= 2
                    h += h_map[s[i]]
            else:
                h <<= 2
                h -= shift * h_map[s[start-1]]
                h += h_map[s[start+9]]

            if h in seen:
                repeats.add(s[start:start+10])
            else:
                seen.add(h)

        return list(repeats)


s = Solution()

inputs = [
    "AAAAAAAAAAA",
]

for i in inputs:
    print s.findRepeatedDnaSequences(i)
