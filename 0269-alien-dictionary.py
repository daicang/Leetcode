from typing import List
from collections import defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        partial_orders = {}
        stack = [words]

        # extract partial orders
        while stack:
            tmp = []
            ws = stack.pop()
            # print('ws:', ws)

            for i, word in enumerate(ws):
                ch = word[0]
                if ch not in partial_orders:
                    partial_orders[ch] = set()

                if i == 0:
                    prev = ch

                if ch != prev:
                    partial_orders[prev].add(ch)
                    stack.append(tmp)
                    tmp = []
                else:
                    if len(word) == 1 and len(tmp) > 0:
                        # 'ab' must be in front of 'abc'
                        return ''

                if len(word) > 1:
                    tmp.append(word[1:])

                if i == len(ws) -1:
                    stack.append(tmp)

                prev = ch

        # generate total order
        reversed_total_order = []

        # print(partial_orders)

        while partial_orders:
            # find the character which has no descendant
            lastone = None
            for pre in partial_orders:
                for desc in partial_orders[pre]:
                    if not partial_orders.get(desc):
                        # found the last descendant
                        lastone = desc
                        break
                if lastone:
                    break

            if lastone is None:
                for key in partial_orders:
                    if len(partial_orders[key]) == 0:
                        reversed_total_order.append(key)
                    else:
                        # no last descendant, cycle
                        print('cycle', partial_orders)
                        return ''
                break

            reversed_total_order.append(lastone)

            if lastone in partial_orders:
                assert len(partial_orders[lastone]) == 0
                del partial_orders[lastone]

            # remove lastone from partial map descendants
            for key in partial_orders:
                if lastone in partial_orders[key]:
                    partial_orders[key].remove(lastone)

        return ''.join(reversed_total_order[::-1])


s = Solution()

inputs = [
    ["wrt","wrf","er","ett","rftt"],
    ["z","x"],
    ["z","x","z"],
    ['z', 'z'],
    ["ab","adc"],
    ['abc', 'ab'], # should be invalid
]

for i in inputs:
    print(s.alienOrder(i))
