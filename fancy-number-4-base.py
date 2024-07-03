
# Number if fancy if its 4-based form only consists 1 and 0s.
# Write a function to find how many positive fancy numbers are there < n.
# For ex:
# 1 => 0
# 10 '1010' => 3 (1, 4, 5)
#  6 '110'  => 3 (1, 4, 5)

def to_4b(n):
    ret = []  # low to high
    while n:
        n, r = divmod(n, 4)
        ret.append(r)
    if not ret:
        return [0]
    return ret


def fancy_4(n):
    n = n - 1  # find i <= n then
    if n < 1:
        return 0

    # Convert to 4-based digits, high to low
    digits = []
    while n:
        n, r = divmod(n, 4)
        digits.append(r)
    digits.reverse()

    count = 1
    has_l1_number = False  # has number > 1

    for d in digits:
        # d could be 0, 1, 2, 3
        # for non-0 digit, count = count * 2
        # but for 0, count = count * 2 - 1
        count *= 2
        if d > 1:
            has_l1_number = True
        elif d == 0:
            if not has_l1_number:
                count -= 1

    return count - 1  # exclude 0


def verify_fancy_4(n):
    count = 0

    def is_fancy(m):
        while m:
            m, r = divmod(m, 4)
            if r != 0 and r != 1:
                return False
        return True

    for i in range(1, n):
        if is_fancy(i):
            count += 1

    f4 = fancy_4(n)
    if f4 != count:
        print(n, count, f4)


for i in range(1, 3000):
    verify_fancy_4(i)

print('done!')
