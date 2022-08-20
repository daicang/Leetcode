from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        tokens = []
        i = 0
        while i < len(expression):
            ch = expression[i]
            if ch.isdigit():
                val = 0
                while i < len(expression) and expression[i].isdigit():
                    val *= 10
                    val += int(expression[i])
                    i += 1
                tokens.append(val)
            else:
                tokens.append(expression[i])
                i += 1

        cache = {}
        result = {}

        def op(left, right, operator):
            match operator:
                case '+':
                    return left + right
                case '-':
                    return left - right
                case '*':
                    return left * right
                case _:
                    assert False

        def compute(begin, end):
            key = (begin, end)
            if key in cache:
                return cache[key]

            if begin == end:
                assert type(tokens[begin]) == int
                return [tokens[begin]]

            results = []
            for i in range(begin, end+1):
                token = tokens[i]
                if type(token) == int:
                    continue
                left = compute(begin, i-1)
                right = compute(i+1, end)

                for l in left:
                    for r in right:
                        results.append(op(l, r, token))

            cache[key] = results
            return results

        return compute(0, len(tokens)-1)

s = Solution()

inputs = [
    "2-1-1",
    "2*3-4*5",
]

for i in inputs:
    print(s.diffWaysToCompute(i))
