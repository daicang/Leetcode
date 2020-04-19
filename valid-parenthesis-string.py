class Solution:
    def checkValidString(self, s: str) -> bool:
        left_count = 0
        star_count = 0
        for char in s:
            if char == '(':
                left_count += 1
            elif char == '*':
                star_count += 1
            else:
                if left_count > 0:
                    left_count -= 1
                elif star_count > 0:
                    star_count -= 1
                else:
                    return False

        if left_count == 0:
            return True

        right_count = 0
        star_count = 0
        for char in s[::-1]:
            if char == ')':
                right_count += 1
            elif char == '*':
                star_count += 1
            else:
                if right_count > 0:
                    right_count -= 1
                elif star_count >0:
                    star_count -= 1
                else:
                    return False

        return True