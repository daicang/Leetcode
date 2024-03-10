from typing import List

class Solution:
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
