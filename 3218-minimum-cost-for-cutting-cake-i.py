class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # Greedy
        # time: O(m+n)
        # space: can by O(1)
        # 1. Order does not matter for consective h/v cuts
        # 2. For h-v and v-h cuts, the cost is h+v+v and v+h+h, max(h, v) go first
        # 3. cost for each cut is cut(h) + extra(sum(v))

        hcuts = sorted(horizontalCut, reverse=True)
        vcuts = sorted(verticalCut, reverse=True)

        hsum = sum(hcuts)
        vsum = sum(vcuts)
        cost = 0

        hi = vi = 0
        while hi < len(hcuts) and vi < len(vcuts):
            if hcuts[hi] > vcuts[vi]:
                # do hcut
                cost += hcuts[hi] + vsum
                hsum -= hcuts[hi]
                hi += 1
            else:
                cost += vcuts[vi] + hsum
                vsum -= vcuts[vi]
                vi += 1

        cost += hsum + vsum
        return cost
