class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cost = 0
        h = []
        i1, i2 = 0, len(costs)-1
        for _ in range(candidates):
            if i1 <= i2:
                heapq.heappush(h, (costs[i1], i1))
                i1 += 1
            if i1 <= i2:
                heapq.heappush(h, (costs[i2], i2))
                i2 -= 1
            if i1 > i2:
                break

        for _ in range(k):
            c, i = heapq.heappop(h)
            cost += c
            if i1 <= i2:
                if i < i1:
                    heapq.heappush(h, (costs[i1], i1))
                    i1 += 1
                else:
                    heapq.heappush(h, (costs[i2], i2))
                    i2 -= 1
        return cost
