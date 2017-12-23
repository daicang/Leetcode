class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def two_sum_closest(l, t):
            def update_delta(ndelta):
                if abs(ndelta) > delta:
                    return delta, is_delta_nega
                else:
                    if ndelta < 0:
                        return -ndelta, True
                    else:
                        return ndelta, False

            half = t / 2.0
            l1 = [x-half for idx, x in enumerate(l) if marked[idx] == 0]

            if len(l1) < 2:
                return None

            nega = [x for x in l1 if x < 0]
            posi = [x for x in l1 if x >= 0]

            if not nega:
                return posi[0] + posi[1] + t

            if not posi:
                return nega[-2] + nega [-1] + t

            delta = nega[-1] + posi[0]
            is_delta_nega = True if delta < 0 else False
            delta = abs(delta)

            if len(nega) > 1:
                delta, is_delta_nega = update_delta(nega[-1] + nega[-2])

            if len(posi) > 1:
                delta, is_delta_nega = update_delta(posi[0] + posi[1])

            for idx, p in enumerate(posi):
                for n in nega:
                    s = p + n
                    if s > 0:
                        delta, is_delta_nega = update_delta(s)
                        break
                    elif s < 0:
                        delta, is_delta_nega = update_delta(s)
                    else:
                        return t

            if is_delta_nega:
                delta *= -1

            return t + delta

        nums.sort()
        marked = {idx: 0 for idx in xrange(len(nums))}
        closest = nums[0] + nums[1] + nums[2]

        for idx, n in enumerate(nums):
            marked[idx] = 1
            two_sum = two_sum_closest(nums, target-n)
            if two_sum is None:
                break

            n_closest = n + two_sum
            if abs(n_closest - target) < abs(closest - target):
                closest = n_closest

        return int(closest)



s = Solution()
print('should be 13', s.threeSumClosest([1, 2, 5, 10, 11], 12))
print('should be 2', s.threeSumClosest([-1,0,1,1,55], 3))
