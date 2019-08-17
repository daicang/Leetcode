class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import defaultdict
        target = defaultdict(int)
        for ch in t:
            target[ch] += 1

        def contain_all(d):
            for val in d.values():
                if val > 0:
                    return False
            return True

        window_size = None
        min_window = None

        l = r = 0
        last_l = 0
        for r, rval in enumerate(s):
            if rval not in target:
                continue
            target[rval] -= 1
            if contain_all(target):
                # print 'r=%s' % r
                # strip left
                l = last_l
                while s[l] not in target or target[s[l]] != 0:
                    if s[l] in target:
                        assert target[s[l]] < 0
                        target[s[l]] += 1
                    l += 1
                last_l = l
                # print 'l=%s, %s' % (l, s[l:r+1])
                if window_size is None or (r-l+1) < window_size:
                    window_size = r - l + 1
                    min_window = s[l:r+1]
                    # print 'window=%s' % s[l:r+1]

        return min_window or ''

s = Solution()

inputs = [
    ['ADOBECODEBANC', 'ABC']
]

for i in inputs:
    print s.minWindow(*i)
