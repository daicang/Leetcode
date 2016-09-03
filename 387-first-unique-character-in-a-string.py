class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = [0] * 26
        last_idx = [0] * 26
        for i, ch in enumerate(s):
            counter[ord(ch) - ord('a')] += 1
            last_idx[ord(ch) - ord('a')] = i

        uniq_idxs = [last_idx[i] for i in
                     filter(lambda i: counter[i] == 1, xrange(26))]
        return min(uniq_idxs) if uniq_idxs else -1
