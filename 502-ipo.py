class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        h = []
        n = len(profits)
        res = list(zip(capital, profits))
        # cost from low to high
        res.sort(key=lambda x: x[0])
        i = 0

        for i, (c, p) in enumerate(res):
            if c <= w:
                # cost ok, use heap to find best profit
                heapq.heappush(h, -p)
            else:
                break

        for _ in range(k):
            if not h:
                break
            p = -heapq.heappop(h)
            w += p
            # now include higher cost
            while i < n and res[i][0] <= w:
                heapq.heappush(h, -res[i][1])
                i += 1

        return w
