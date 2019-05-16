class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        length = len(A)
        left = 0
        right = 0
        prefix = 0
        k_count = 0
        counter = {}

        def inc(val):
            if val in counter:
                counter[val] += 1
            else:
                counter[val] = 1

        def dec(val):
            if counter[val] == 1:
                del counter[val]
            else:
                counter[val] -= 1

        for right in range(length):
            inc(A[right])
            # sliding window
            if A[right] == A[left]:
                for i in range(left, right+1):
                    if counter[A[i]] > 1:
                        dec(A[i])
                        prefix += 1
                    else:
                        left = i
                        break
                if len(counter) == K:
                    k_count += prefix + 1
            else:
                if len(counter) == K:
                    k_count += prefix + 1

                elif len(counter) > K:
                    prefix = 0
                    dec(A[left])
                    left += 1
                    # Now len(counter) == K
                    for i in range(left, right+1):
                        if counter[A[i]] > 1:
                            dec(A[i])
                            prefix += 1
                        else:
                            left = i
                            break
                    # assert len(counter) == K
                    k_count += prefix + 1

        return k_count


s = Solution()

inputs = [
    [[1,2,1,2,3], 2],  # 7
    [[1,2,1,3,4], 3],  # 3
    [[1,1,2], 1], # 4
    [[1, 2], 1], # 2
    [[27,27,43,28,11,20,1,4,49,18,37,31,31,7,3,31,50,6,50,46,4,13,31,49,15,52,25,31,35,4,11,50,40,1,49,14,46,16,11,16,39,26,13,4,37,39,46,27,49,39,49,50,37,9,30,45,51,47,18,49,24,24,46,47,18,46,52,47,50,4,39,22,50,40,3,52,24,50,38,30,14,12,1,5,52,44,3,49,45,37,40,35,50,50,23,32,1,2], 20],
]

for i in inputs:
    print(s.subarraysWithKDistinct(*i))

