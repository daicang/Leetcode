
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        for i in range(len(graph)):
            if i not in color:
                color[i] = False
                stack = [i]
                while stack:
                    node = stack.pop()
                    nei_color = not color[node]
                    for nei in graph[node]:
                        if nei in color:
                            if color[nei] != nei_color:
                                return False
                        else:
                            color[nei] = nei_color
                            stack.append(nei)

        return True
