
def solver1(a, b):
    # time: O(n^2)
    # space: O(n)
    n = len(a)

    # Gaussian elimination to lower triangle matrix
    for i in range(n-1, 0, -1):
        if a[i][i] == 0:
            # Swap with non-zero row
            for j in range(i):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    b[i], b[j] = b[j], b[i]
        # Eliminate a[0..i-1][i]
        for j in range(i):
            multiplier = a[j][i] / a[i][i]
            for k in range(i+1):
                a[j][k] -= multiplier * a[i][k]
            b[j] -= multiplier * b[i]

    # Verify triangle
    for i in range(n):
        for j in range(i+1, n):
            assert a[i][j] == 0

    # Solve lower triangle matrix
    result = []
    for i in range(n):
        val = b[i]
        for j in range(i):
            val -= a[i][j] * result[j]
        val /= a[i][i]
        result.append(val)

    return result


def solver2(a, b):
    # a: n x n, [[1]], [[1,2],[1,2]]
    # time: O(n^3)
    # space: O(n^3)
    n = len(a)
    if n == 1:
        return [b[0] / a[0][0]]

    for i in range(n):
        row = a[i]
        if row[-1] != 0:
            # swap with last new_row
            a[-1], a[i] = a[i], a[-1]
            b[-1], b[i] = b[i], b[-1]
            break

    assert a[-1][-1] != 0

    last_row = a[-1]
    last_b = b[-1]
    new_a = []
    new_b = []

    for r in range(n-1):
        row = a[r]
        new_row = []
        multiplier = row[-1] / last_row[-1]
        for i, val in enumerate(row):
            if i != len(row)-1:
                new_row.append(val - last_row[i] * multiplier)
        new_a.append(new_row)
        new_b.append(b[r] - last_b * multiplier)

    assert len(new_a) == n-1
    assert len(new_b) == n-1

    solved = solver2(new_a, new_b)
    # now solved [1 .. n-1]
    assert len(solved) == n-1

    row = a[-1]
    x = b[-1]
    for i, val in enumerate(solved):
        x -= val * row[i]
    solved.append(x / row[-1])

    return solved

test_cases = [
    [
        [[1]],
        [2]
    ],

    [
        [[1, 1],
        [1, 0]],
        [2, 1]
    ],

    [
        [
            [1, 2, 3],
            [1, 2, 5 ],
            [2, 3, 4 ]
        ],
        [ 5, 6, 7 ]
    ],

    [
        [
            [ 1, 2, 3, 4  ],
            [ 1, 2, 5, 10  ],
            [ 2, 3, 4, 2  ],
            [ 5, 6, 7, 8  ]
        ],
        [ 10, 11, 12, 13 ]
    ],
]

for case in test_cases:
    print(solver1(*case))
    print(solver2(*case))
