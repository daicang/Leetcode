class Solution:
    def twoSum(self, nums, target):
        snums = nums[:]
        l = len(nums)
        ret = []
        i, j = 0, l - 1
        
        snums.sort()
        while i < j:
            sum = snums[i] + snums[j]
            if sum == target:
                for idx in range(l):
                    if nums[idx] == snums[i]:
                        ret.append(idx+1)
                    elif nums[idx] == snums[j]:
                        ret.append(idx+1)
                ret.sort()
                return ret[0], ret[1]
            if sum < target:
                i = i + 1
            else:
                j = j - 1
                

s = Solution()
print(s.twoSum([3, 2, 4], 6))
