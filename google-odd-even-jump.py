class Solution(object):

    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)

        def m_stack(l):
            nexts = [None] * size
            stack = []
            for i in l:
                while stack and i > stack[-1]:
                    nexts[stack.pop()] = i
                stack.append(i)
            return nexts

        idx_in_order = sorted(range(size), key=lambda i: A[i])
        up_next = m_stack(idx_in_order)
        idx_in_order.sort(key=lambda i: -A[i])
        down_next = m_stack(idx_in_order)

        go_up = [0] * size
        go_down = [0] * size
        go_up[-1] = 1
        go_down[-1] = 1
        for start in range(size-2, -1, -1):
            if up_next[start] is not None:
                go_up[start] = go_down[up_next[start]]
            if down_next[start] is not None:
                go_down[start] = go_up[down_next[start]]

        return sum(go_up)



    # TLE
    def oddEvenJumps_1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)

        go_up = [0] * size
        go_down = [0] * size
        go_up[-1] = 1
        go_down[-1] = 1

        for start in range(size-2, -1, -1):
            last_up = None
            last_down = None
            for end in range(start+1, size):
                if A[end] >= A[start]:
                    if last_up is None or A[end] < A[last_up]:
                        last_up = end
                        go_up[start] = go_down[end]

                if A[end] <= A[start]:
                    if last_down is None or A[end] > A[last_down]:
                        last_down = end
                        go_down[start] = go_up[end]

        return sum(go_up)



s = Solution()

inputs = (
    [10,13,12,14,15],  # 2
    [2,3,1,1,4],  # 3
    [5,1,3,4,2],  # 3
    [1,2,3,2,1,4,4,5], # 6
)

for input in inputs:
    print('input: %s' % input)
    print(s.oddEvenJumps(input))
