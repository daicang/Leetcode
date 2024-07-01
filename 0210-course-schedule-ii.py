from typing import List
from collections import defaultdict

class Solution:
    def findOrder_ts(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sorting
        # space: O(n), time: O(n)
        prevs = {}
        nexts = {}
        for i in range(numCourses):
            prevs[i] = set()
            nexts[i] = set()

        for curr, prev in prerequisites:
            prevs[curr].add(prev)
            nexts[prev].add(curr)

        heads = []  # heads are those with 0 prevs
        for p, nodes in prevs.items():
            if len(nodes) == 0:
                heads.append(p)

        order = []
        while heads:
            new_heads = []
            for head in heads:
                order.append(head)
                for node in nexts[head]:
                    prevs[node].remove(head)
                    if len(prevs[node]) == 0:
                        new_heads.append(node)
                del prevs[head]
                del nexts[head]
            heads = new_heads

        if len(prevs) == 0:
            # can be serialized
            return order
        return []


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = []
        for i in range(numCourses):
            graph.append([])

        for course, dependency in prerequisites:
            graph[course].append(dependency)

        visited = [False] * numCourses
        path = [False] * numCourses
        order = []

        def traverse(i):
            if path[i]:
                return False
            if visited[i]:
                return True
            visited[i] = True
            path[i] = True
            for node in graph[i]:
                if traverse(node) is False:
                    return False
            order.append(i)
            path[i] = False
            return True

        for i in range(numCourses):
            if traverse(i) is False:
                return []

        return order

s = Solution()

inputs = [
    [4, [[1,0],[2,0],[3,1],[3,2]]],
]

for i in inputs:
    print(s.findOrder(*i))
