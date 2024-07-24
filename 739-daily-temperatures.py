class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temp)

        for i, val in enumerate(temp):
            while stack and temp[stack[-1]] < val:
                j = stack.pop()
                answer[j] = i-j
            stack.append(i)

        return answer
