
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        n, target = len(graph), len(graph)-1
        visited = [False] * n

        def dfs(node, path):
            if node == target:
                paths.append(path+[target])
                return

            path.append(node)
            visited[node] = True
            for next_node in graph[node]:
                if not visited[next_node]:
                    dfs(next_node, path)
            visited[node] = False
            path.pop()

        dfs(0, [])
        return paths
