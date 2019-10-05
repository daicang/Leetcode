class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        memo = {}

        def solve(s_):
            if s_ not in memo:
                encoded = [s_]
                substr_end_index = (s_ + s_).find(s_, 1)
                if substr_end_index != len(s_):
                    encoded.append('%s[%s]' % (len(s_)/substr_end_index, solve(s_[:substr_end_index])))

                encoded.extend([(solve(s_[:i])+solve(s_[i:])) for i in range(1, len(s_))])

                memo[s_] = min(encoded, key=len)
            return memo[s_]

        return solve(s)


s = Solution()

inputs = [
    "aaaaaaaaaa",
    "abbbabbbcabbbabbbc",
    "aabcaabcd",
    "aaa"
]

for i in inputs:
    print s.encode(i)
