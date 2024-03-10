
from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = []
        for _ in range(n):
            graph.append([])

        for n1, n2 in dislikes:
            graph[n1-1].append(n2-1)
            graph[n2-1].append(n1-1)

        color = [None] * n

        for i in range(n):
            if color[i] is None:
                color[i] = 0
                stack = [i]
                while stack:
                    node = stack.pop()
                    next_color = color[node] ^ 1
                    for nei in graph[node]:
                        if color[nei] != None:
                            if color[nei] != next_color:
                                return False
                        else:
                            color[nei] = next_color
                            stack.append(nei)

        return True
