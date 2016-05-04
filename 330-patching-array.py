# 330-patching-array.py

class Solution(object):
    def minPatches_wa(self, nums, n): # Wrong answer. not this method.
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # Example:
        # nums = [1, 2, 4, 9]
        # rbound = 1 + 2 + 4 = 7
        
        count = 0
        toInsert = 2
        rbound = 1
        size = len(nums)

        if size == 0 or nums[0] != 1:
            nums.insert(0, 1)
            count += 1

        insert_idx = 1 # nums[0] is always 1
        
        while rbound < n:
            print "r: ", rbound, " count: ", count
            while insert_idx < size:
                curr = nums[insert_idx]
                if curr == toInsert:
                    rbound += curr
                    insert_idx += 1
                    toInsert *= 2
                elif curr <= rbound:
                    rbound += curr
                    insert_idx += 1
                else: 
                    break

            if rbound >= n: break

            nums.insert(insert_idx, toInsert)
            count += 1
            rbound += toInsert
            toInsert *= 2
            insert_idx += 1
            size += 1

        print nums
        return count

    def minPatches(self, nums, n):
        count, top = 0, 0
        i = 0

        while top < n:
            if i < len(nums) and nums[i] <= top + 1:
                top += nums[i]
                i += 1
            else:
                print 'top: ', top, ' count: ', count
                top = top * 2 + 1
                count += 1

        return count

s = Solution()

print s.minPatches([1,5,10], 20)
print s.minPatches([1,2,2], 5)

print s.minPatches([1,2,31,33], 2147483647)
