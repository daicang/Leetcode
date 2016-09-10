import collections


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        starti = 0
        maxlen = 0
        l = len(s)
        counter = collections.defaultdict(int)
        incomplete = collections.defaultdict(int)

        while starti < l-k:
            counter.clear()
            incomplete.clear()
            nexti = starti + 1
            for endi in xrange(starti, l):
                ch = s[endi]
                counter[ch] += 1

                if counter[ch] < k:
                    incomplete[ch] = 1
                elif counter[ch] >= k:
                    incomplete[ch] = 0
                    if sum(incomplete.itervalues()) == 0:
                        maxlen = max(maxlen, endi - starti + 1)
                        nexti = endi + 1
            starti = nexti
        return maxlen
