from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = []
        for i in range(numCourses):
            graph.append([])

        for course, dependency in prerequisites:
            graph[course].append(dependency)

        checked = [False] * numCourses
        path = [False] * numCourses

        def traverse(i):
            if path[i]:
                return False

            if checked[i]:
                return True
            checked[i] = True

            path[i] = True
            for dep in graph[i]:
                if traverse(dep) is False:
                    return False
            path[i] = False
            return True

        for i in range(numCourses):
            if traverse(i) is False:
                return False

        return True

s = Solution()

inputs = [
    [2, [[1,0]]],
    [4, [[0,1],[3,1],[1,3],[3,2]]]
]

for i in inputs:
    print(s.canFinish(*i))