class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False] * n

        @cache
        def traverse(i):
            # DFS
            if visited[i]:
                return False
            visited[i] = True
            for ni in graph[i]:
                if traverse(ni) is False:
                    visited[i] = False
                    return False
            visited[i] = False
            return True

        safes = []
        for i in range(n):
            if traverse(i):
                safes.append(i)

        return safes
