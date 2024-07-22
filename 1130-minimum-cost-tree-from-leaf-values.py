class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        count = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            count += min(arr[i-1:i] + arr[i+1:i+2]) * arr.pop(i)
        return count

    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        count = 0
        for i, n in enumerate(arr):
            while stack[-1] <= n:
                mid = stack.pop()
                count += mid * min(stack[-1], n)
            stack.append(n)
        while len(stack) > 2:
            count += stack.pop() * stack[-1]
        return count