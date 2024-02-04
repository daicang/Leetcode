

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n == 0:
            return 0
        digits = []  # digits, in reverse order
        while n > 0:
            digits.append(n % 10)
            n //= 10

        counter = [0] * 10
        for i, n in enumerate(digits):
            counter[n] += 1
            if i > 0 and n < digits[i-1]:  # when visiting in reversed order, digit is less than last digit
                for j in range(n+1, 10):
                    if counter[j] > 0:  # replace with first larger digit appeared
                        counter[j] -= 1
                        digits[i] = j
                        break
                high = digits[i:]  # high part, reversed order
                low = []  # low part, in order
                for i, count in enumerate(counter):
                    for _ in range(count):
                        low.append(i)
                new_digit = high[::-1] + low
                new_value = 0
                for d in new_digit:
                    new_value *= 10
                    new_value += d
                if new_value > (2**31)-1:
                    return -1
                return new_value
        return -1


    def nextGreaterElement_i(self, n: int) -> int:
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
