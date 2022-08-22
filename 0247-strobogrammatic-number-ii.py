from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        sb_table = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }

        def generate_left(n):
            ret = []
            for i in range(n):
                if i == 0:
                    for ch in sb_table.keys():
                        if ch != '0':
                            ret.append([ch])
                else:
                    tmp = []
                    for s in ret:
                        for ch in sb_table.keys():
                            tmp.append(s+[ch])
                    ret = tmp
            return ret

        def generate_middle(sbs):
            ret = []
            for s in sbs:
                for lval, rval in sb_table.items():
                    if lval == rval:
                        ret.append(s+[lval])
            return ret

        def generate_right(sbs, has_middle):
            for i, left in  enumerate(sbs):
                right = left[::-1]
                if has_middle:
                    right = right[1:]
                for j, ch in enumerate(right):
                    right[j] = sb_table[ch]
                sbs[i] = left + right

        if n == 1:
            # only left
            return ['0', '1', '8']

        left, mid = divmod(n, 2)

        sbs = generate_left(left)
        if mid:
            sbs = generate_middle(sbs)
        generate_right(sbs, mid)

        return [''.join(s) for s in sbs]

s = Solution()

inputs = [
    1,
    2,
    3,
    4,
]

for i in inputs:
    print(s.findStrobogrammatic(i))
