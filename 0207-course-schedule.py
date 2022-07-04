from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep_map = []
        for i in range(numCourses):
            dep_map.append([])


        for req in prerequisites:
            curr, dep = req[0], req[1]
            dep_map[curr].append(dep)

        for i in range(numCourses):
            checked = [False] * numCourses
            pres = dep_map[i]
            while pres:
                curr = pres.pop()
                if curr == i:
                    return False
                if checked[curr]:
                    continue
                checked[curr] = True
                pres.extend(dep_map[curr])

        return True

s = Solution()

inputs = [
    [2, [[1,0]]],
    [4, [[0,1],[3,1],[1,3],[3,2]]]
]

for i in inputs:
    print(s.canFinish(*i))