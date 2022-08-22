from typing import List
from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strings:
            shift = ord(s[0]) - ord('a')
            tmp = []
            for ch in s:
                idx = ord(ch) - ord('a') - shift
                if idx < 0: idx += 26
                tmp.append(idx)
            key = tuple(tmp)
            groups[key].append(s)

        return list(groups.values())

inputs = [
    ["abc","bcd","acef","xyz","az","ba","a","z"],
    ['a'],
]

s = Solution()

for i in inputs:
    print(s.groupStrings(i))
