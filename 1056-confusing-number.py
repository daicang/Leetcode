class Solution:
    def confusingNumber(self, n: int) -> bool:
        if n == 0:
            return False

        numbers = []
        valid = [False] * 10
        for i in (0,1,6,8,9):
            valid[i] = True

        while n:
            n, r = divmod(n, 10)
            numbers.append(r)

        i, j = 0, len(numbers)-1
        diff = False

        while i < j:
            if (not valid[numbers[i]]) or (not valid[numbers[j]]):
                return False
            if numbers[i] != numbers[j] and numbers[i] + numbers[j] != 15:
                diff = True
            i += 1
            j -= 1
        if not valid[numbers[i]]:
            return False
        if numbers[i] in (6, 9):
            diff = True

        return diff
