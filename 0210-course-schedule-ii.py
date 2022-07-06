from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        successors = [None] * numCourses
        order = []
        pres = [0] * numCourses

        for pre in prerequisites:
            successor, precursor = pre[0], pre[1]
            if successors[precursor] is None:
                successors[precursor] = [successor]
            else:
                successors[precursor].append(successor)
            pres[successor] += 1

        no_pre = []

        for course, value in enumerate(pres):
            if value == 0:
                no_pre.append(course)

        while no_pre:
            course = no_pre.pop()
            order.append(course)
            if successors[course]:
                for suc in successors[course]:
                    pres[suc] -= 1
                    if pres[suc] == 0:
                        no_pre.append(suc)

        if sum(pres) > 0:
            return []

        return order

s = Solution()

inputs = [
    [4, [[1,0],[2,0],[3,1],[3,2]]],
]

for i in inputs:
    print(s.findOrder(*i))
