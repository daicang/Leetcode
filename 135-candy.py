class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        if len(ratings) == 1:
            return 1

        candies = [None] * len(ratings)
        queue = []

        for i, val in enumerate(ratings):
            if i == 0 and ratings[0] <= ratings[1]:
                queue.append(0)

            elif i == len(ratings)-1 and ratings[-1] <= ratings[-2]:
                queue.append(i)

            else:
                if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                    queue.append(i)

        while queue:
            # print candies
            i = queue[0]
            queue = queue[1:]
            if candies[i] is not None:
                continue

            r = ratings[i]
            if i > 0:
                r_before = ratings[i-1]
            else:
                r_before = r

            if i < len(ratings)-1:
                r_after = ratings[i+1]
            else:
                r_after = r

            if r <= r_before:
                if r <= r_after:
                    candies[i] = 1
                else:
                    # r-before = r > r-after
                    if candies[i+1] is not None:
                        candies[i] = candies[i+1] + 1

            else:
                # r_before < r
                if  candies[i-1] is not None:
                    if r > r_after:
                        if candies[i+1]:
                            candies[i] = max(candies[i-1], candies[i+1]) + 1
                    else:  # r_before < r <= r_after
                        candies[i] = candies[i-1] + 1

            if i > 0 and candies[i-1] is None:
                queue.append(i-1)

            if i < len(ratings)-1 and candies[i+1] is None:
                queue.append(i+1)

        # print candies
        return sum(candies)


s = Solution()
inputs = [
    [1,0,2],  # 5
    [1,2,2], # 4
    [29,51,87,87,72,12],
    [1,6,10,8,7,3,2],  # 18
    [1,2,3],
]

for i in inputs:
    print s.candy(i)
