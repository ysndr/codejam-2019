import sys


def get_digit(number, n):
    if 10**n > number:
        return -1
    else:
        return number // 10**n % 10

def has_four_at(number):
    fours_idx = []
    d = 0

    digit = get_digit(number, d)
    while digit != -1:
        if digit == 4:
            fours_idx.append(d)
        d += 1
        digit = get_digit(number, d)
    
    return fours_idx

def generate_b(fours_idx):
    b = 0
    for idx in fours_idx:
        b += 10**idx
    return b

input()
i = 1
for line in sys.stdin:
    if line == "\n":
        break
    N = int(line.rstrip())
    

    fours_idx = has_four_at(N)
    B = generate_b(fours_idx)

    A = N - B

    print("Case %s: %s %s" % (i, A, B))
    
    i += 1
