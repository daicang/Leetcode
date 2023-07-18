

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        digits = [int(ch) for ch in digits]
        digits = digits[::-1]
        counter = [0] * 10

        for i, val in enumerate(digits):
            counter[val] += 1
            for j in range(val+1, 10):
                if counter[j] > 0:
                    counter[j] -= 1
                    return self.gen_greater_num(counter, j, digits[i+1:])
        return -1


    def gen_greater_num(self, counter, val, rest):
        # num = <counter, large-to-small> <val> <rest>
        # return reverse(num)
        digits = []
        for i in range(10):
            for _ in range(counter[i]):
                digits.append(i)
        digits = digits[::-1]
        digits.append(val)
        digits.extend(rest)
        digits = digits[::-1]

        ret = 0
        for d in digits:
            ret *= 10
            ret += d

        if ret > (2**31)-1:
            return -1
        return ret
