
from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = []
        for _ in range(n):
            graph.append([])

        for s, d, price in flights:
            graph[s].append((price, d))

        prices = [float('inf')] * n
        stops = [k+1] * n

        h = []
        for price, d in graph[src]:
            heapq.heappush(h, (price, d, 0))

        while h:
            price, pos, stop = heapq.heappop(h)
            if pos == dst:
                return price

            prices[pos] = price
            stops[pos] = min(stops[pos], stop)

            if stop < k:
                stop += 1
                for cost, next_dst in graph[pos]:
                    new_price = price + cost
                    # Must pruning
                    if new_price < prices[next_dst] or stop < stops[next_dst]:
                        heapq.heappush(h, (new_price, next_dst, stop))

        return -1

s = Solution()

data = [
    [4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1],
    [3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1],
    [11, [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]], 0, 2, 4],  # 11
]

for d in data:
    print(s.findCheapestPrice(*d))
