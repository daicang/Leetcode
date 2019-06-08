class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        orders = []
        zero_positions = set((tuple(m) for m in mines))
        max_order = 0
        for _ in range(N):
            orders.append([N] * N)

        for row in range(N):
            count = 0
            for col in range(N):
                count += 1
                if (row, col) in zero_positions:
                    count = 0
                orders[row][col] = count

            count = 0
            for col in range(N-1, -1, -1):
                count += 1
                if (row, col) in zero_positions:
                    count = 0
                orders[row][col] = min(orders[row][col], count)

        for col in range(N):
            count = 0
            for row in range(N):
                count += 1
                if (row, col) in zero_positions:
                    count = 0
                orders[row][col] = min(orders[row][col], count)

            count = 0
            for row in range(N-1, -1, -1):
                count += 1
                if (row, col) in zero_positions:
                    count = 0
                orders[row][col] = min(orders[row][col], count)
                max_order = max(max_order, orders[row][col])

        # for l in orders:
        #     print l

        return max_order


s = Solution()
print(s.orderOfLargestPlusSign(5, [[4,2]]))
