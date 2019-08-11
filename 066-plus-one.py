class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for idx in range(len(digits)-1, -1, -1):
            digits[idx] += 1
            if digits[idx] < 10:
                break
            digits[idx] = 0
        else:
            digits.insert(0, 1)

        return digits