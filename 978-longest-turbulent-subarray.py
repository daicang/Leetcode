class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        greater, eq, less = 'g', 'e', 'l'
        if len(arr) < 2:
            return len(arr)
        max_size = 1
        last_size = 1
        last_sign = eq
        last_n = arr[0]

        for i, n in enumerate(arr):
            if i == 0: continue
            if n == last_n:
                sign = eq
            elif n > last_n:
                sign = greater
            else:
                sign = less

            if sign == eq:
                last_size = 1
            elif sign == greater:
                if last_sign == less:
                    last_size += 1
                else:
                    last_size = 2
            else:
                if last_sign == greater:
                    last_size += 1
                else:
                    last_size = 2
            max_size = max(max_size, last_size)
            last_n = n
            last_sign = sign

        return max_size
