
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        visited = [False] * len(graph)

        def dfs(node, path):
            if node == len(graph)-1:
                paths.append(path[:])
            else:
                visited[node] = True
                for next_node in graph[node]:
                    if not visited[next_node]:
                        path.append(next_node)
                        dfs(next_node, path)
                        path.pop()
                visited[node] = False

        dfs(0, [0])

        return paths
