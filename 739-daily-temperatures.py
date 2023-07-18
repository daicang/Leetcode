from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = [0] * len(temperatures)

        for i, value in enumerate(temperatures):
            while stack and stack[-1][1] < value:
                j = stack.pop()[0]
                days[j] = i - j
            stack.append((i, value))

        return days
