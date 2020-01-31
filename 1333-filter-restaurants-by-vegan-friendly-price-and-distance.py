from typing improt List

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        # [id, rating, vegan, price, distance]
        ret = []
        for r in restaurants:
            if veganFriendly and not r[2]:
                continue
            if r[3] > maxPrice or r[4] > maxDistance:
                continue
            ret.append(r)

        ret.sort(key=lambda x: (x[1], x[0]), reverse=True)
        return [r[0] for r in ret]

