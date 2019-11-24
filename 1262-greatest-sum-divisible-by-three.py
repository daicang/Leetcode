class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums) + 1  # dp array index = num index + 1
        dp_r0 = [0] * size
        dp_r1 = [0] * size
        dp_r2 = [0] * size

        for i, num in enumerate(nums):
            remain = num % 3
            if remain == 0:
                dp_r0[i+1] = dp_r0[i] + num
                if dp_r1[i] > 0:
                    dp_r1[i+1] = dp_r1[i] + num
                if dp_r2[i] > 0:
                    dp_r2[i+1] = dp_r2[i] + num

            elif remain == 1:
                if dp_r2[i] > 0:
                    dp_r0[i+1] = max(dp_r0[i], dp_r2[i] + num)
                else:
                    dp_r0[i+1] = dp_r0[i]

                dp_r1[i+1] = max(dp_r0[i] + num, dp_r1[i])

                if dp_r1[i] > 0:
                    dp_r2[i+1] = max(dp_r1[i] + num, dp_r2[i])
                else:
                    dp_r2[i+1] = dp_r2[i]

            else:  # remain == 2
                if dp_r1[i] > 0:
                    dp_r0[i+1] = max(dp_r1[i] + num, dp_r0[i])
                else:
                    dp_r0[i+1] = dp_r0[i]

                if dp_r2[i] > 0:
                    dp_r1[i+1] = max(dp_r1[i], dp_r2[i] + num)
                else:
                    dp_r1[i+1] = dp_r1[i]

                dp_r2[i+1] = max(dp_r0[i] + num, dp_r2[i])

        return dp_r0[-1]


s = Solution()

inputs = [
    [3,6,5,1,8],
    [4],
    [1,2,3,4,4],
    [1,1,4,5,7],

    # 50487
    [366,809,6,792,822,181,210,588,344,618,341,410,121,864,191,749,637,169,123,472,358,908,235,914,322,946,738,754,908,272,267,326,587,267,803,281,586,707,94,627,724,469,568,57,103,984,787,552,14,545,866,494,263,157,479,823,835,100,495,773,729,921,348,871,91,386,183,979,716,806,639,290,612,322,289,910,484,300,195,546,499,213,8,623,490,473,603,721,793,418,551,331,598,670,960,483,154,317,834,352],
]

for i in inputs:
    print s.maxSumDivThree(i)
