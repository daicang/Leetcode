class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        s = 0
        m = 10 ** 9 + 7
        stack = []
        for i, n in enumerate(arr):
            # for each element in stack
            # its previous element is the first lesser element on left side
            # when poped, the coming element is the first lesser element on right side
            while stack and arr[stack[-1]] >= n:
                j = stack.pop()
                left_len = j - stack[-1] if stack else 1
                s += arr[j] * left_len * (i-j)
            stack.append(i)
        while stack:
            j = stack.pop()
            left_len = j - stack[-1] if stack else 1
            right_len = len(arr) - j
            s += arr[j] * left_len * right_len
        return s % m


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        s = 0
        m = 10 ** 9 + 7
        stack = []
        prev_smaller = [None] * len(arr)
        next_smaller = [None] * len(arr)

        for i, n in enumerate(arr):
            while stack and arr[stack[-1]] >= n:
                j = stack.pop()
                next_smaller[j] = i
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        while stack:
            i = stack.pop()
            next_smaller[i] = len(arr)

        for i in range(len(arr)):
            s += arr[i] * (i-prev_smaller[i]) * (next_smaller[i]-i)
        return s % m
