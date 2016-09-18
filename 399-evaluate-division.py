import collections


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def _calc(parentd, curr):
            result = 1
            parent = parentd[curr]
            while parent:
                result *= graph[parent][curr]
                curr = parentd[curr]
                parent = parentd[curr]
            return result

        result = []
        graph = collections.defaultdict(dict)

        for [a, b], val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        for [a, b] in queries:
            if a not in graph:
                result.append(-1.0)
                continue

            visited = set([a])
            parentd = {a: None}
            q = collections.deque([a, None])

            while len(q):
                curr = q.popleft()
                if curr == b:
                    result.append(_calc(parentd, curr))
                    break
                else:
                    for neighbor in graph[curr].keys():
                        if neighbor not in visited:
                            q.append(neighbor)
                            parentd[neighbor] = curr
                            visited.add(neighbor)
            else:
                result.append(-1.0)

        return result

s = Solution()
print s.calcEquation([['a', 'b'], ['b', 'c']], [2.0, 3.0],
                     [['a', 'c'], ['b', 'c'], ['a', 'e'], ['a', 'a'], ['x', 'x']])

print s.calcEquation([['a', 'aa']], [9.0], [['aa', 'a'], ['aa', 'aa']])
