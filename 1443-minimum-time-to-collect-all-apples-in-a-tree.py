
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = []
        for _ in range(n):
            graph.append([])

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = [0] * n

        def solve(i):
            visited[i] = 1
            count = 0
            has_apple = hasApple[i]
            for child in graph[i]:
                if visited[child]:
                    continue
                apple, child_count = solve(child)
                has_apple = has_apple or apple
                count += child_count

            if has_apple:
                count += 2
            visited[i] = 0
            return has_apple, count

        _, mintime = solve(0)
        if mintime > 0:
            return mintime-2

        return 0
