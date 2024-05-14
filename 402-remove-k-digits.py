
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num

        stack = []
        for ch in num:
            digit = int(ch)
            while k > 0 and stack and stack[-1] > digit:
                # if digit > next_digit, remove
                stack.pop()
                k -= 1
            stack.append(digit)

        while stack and k > 0:
            # remove from last digit
            stack.pop()
            k -= 1

        while stack and stack[0] == 0:
            # trim leading zeros
            stack.pop(0)
        if not stack:
            return '0'
        return ''.join([str(d) for d in stack])
