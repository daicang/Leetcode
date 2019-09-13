class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        last_lv_sums = triangle[0]

        for level in triangle[1:]:
            this_lv_sums = []
            for idx, val in enumerate(level):
                if idx == 0:
                    last_sum = last_lv_sums[0]
                elif idx == len(level)-1:
                    last_sum = last_lv_sums[-1]
                else:
                    last_sum = min(last_lv_sums[idx], last_lv_sums[idx-1])
                this_lv_sums.append(val+last_sum)
            last_lv_sums = this_lv_sums

        return min(last_lv_sums)


