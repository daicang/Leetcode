class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(n):
            ret = 0
            power = 0
            if n == 0:
                return mapping[0]
            while n > 0:
                n, r = divmod(n, 10)
                ret += mapping[r] * (10 ** power)
                power += 1
            return ret

        nums.sort(key=convert)
        return nums
