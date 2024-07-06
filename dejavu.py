'''
deja vu: a feeling of having already experienced the present situation.

Olivia has a playlist of unique songs, for example: ['good 4 u', 'traitor', 'drivers license', 'happier']. All her life, she listened to the songs in that order.

Recently, Olivia discovered a shuffle option that plays songs in a random order. When listening to the shuffled playlist, if she hears two songs in a  row that are in the same order as in the original list, then she gets deja vu.

Given Oliva's original playlist of songs, print out all shuffled paylists that will give Oliva deja vu.

'''

inputs = [
    ['good 4 u', 'traitor', 'drivers license', 'happier'],
]

def permutation(data):
    # time: O(n^2)
    # space: O(n^2)
    results = []
    used = [False] * len(data)

    def traverse(path):
        if len(path) == len(data):
            result = []
            for elem in path:
                if isinstance(elem, str):
                    result.append(elem)
                else:
                    result.extend(elem)
            results.append(result)
            return
        for i, val in enumerate(data):
            if used[i] is False:
                used[i] = True
                path.append(val)
                traverse(path)
                path.pop()
                used[i] = False

    traverse([])
    return results


def dejavu(songs):
    # time: O(n^3)
    # space: O(n^3)
    results = []
    n = len(songs)

    for i in range(1, n):
        data = []
        for j in range(n):
            if j == i-1:
                continue
            elif j == i:
                data.append([songs[i-1], songs[i]])
            else:
                data.append(songs[j])
        # print(data)
        results.extend(permutation(data))

    for pl in results:
        print(pl)


for i in inputs:
    dejavu(i)
