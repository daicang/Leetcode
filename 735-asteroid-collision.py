class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            if n > 0:
                stack.append(n)
            else:
                while True:
                    if not stack or stack[-1] < 0:
                        stack.append(n)
                        break
                    if stack[-1] > abs(n):
                        break
                    if stack[-1] == abs(n):
                        stack.pop()
                        break
                    stack.pop()

        return stack
