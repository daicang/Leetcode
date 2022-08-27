
from typing import List

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower_bound = 0
        # monotonic stack
        for val in preorder:
            if val < lower_bound:
                return False
            while stack and val > stack[-1]:
                lower_bound = stack.pop()
            stack.append(val)

        return True


inputs = [
    [2,1],
    [5,2,1,3,6],
    [5,2,6,1,3],
]

s = Solution()

for i in inputs:
    print(s.verifyPreorder(i))
