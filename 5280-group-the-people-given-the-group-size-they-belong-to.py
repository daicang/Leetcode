class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        groups = defaultdict(list)

        def add_to_group(group, size, i):
            last_group = group[-1]
            if len(last_group) < size:
                last_group.append(i)
            else:
                group.append([i])

        for idx, g in enumerate(groupSizes):
            if not groups[g]:
                groups[g] = [[idx]]
            else:
                add_to_group(groups[g], g, idx)

        result = []
        for g in groups.values():
            result.extend(g)

        return result

s = Solution()

data = [
    [3,3,3,3,3,1,3],
    [2,1,3,3,3,2]
]

for d in data:
    print s.groupThePeople(d)
