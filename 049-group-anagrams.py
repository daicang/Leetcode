class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        def str_to_key(s):
            s = [ch for ch in s]
            s.sort()
            return ''.join(s)


        counter = {}
        for s in strs:
            key = str_to_key(s)
            if key in counter:
                counter[key].append(s)
            else:
                counter[key] = [s]

        return counter.values()

