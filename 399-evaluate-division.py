class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        graph = defaultdict(dict)
        n = len(values)
        for i in range(n):
            di, dv = equations[i]
            graph[di][dv] = values[i]
            graph[dv][di] = 1 / values[i]

        for query in queries:
            di, dv = query
            if di not in graph:
                result.append(-1)
                continue
            q = [(di, 1)]
            visited = set()
            while q:
                i, val = q.pop()
                if i == dv:
                    result.append(val)
                    break
                visited.add(i)
                for ni, ratio in graph[i].items():
                    if ni not in visited:
                        q.append((ni, val * ratio))
            else:
                result.append(-1)

        return result
