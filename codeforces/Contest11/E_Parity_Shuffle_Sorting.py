import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        return

    ops = []

    # Step 1: make a[0] == a[n-1]
    ops.append((1, n))
    if (a[0] + a[n - 1]) % 2 == 1:
        # odd sum: a[n-1] := a[0]
        x = a[0]
    else:
        # even sum: a[0] := a[n-1]
        x = a[n - 1]

    # Step 2: force every interior element to equal x
    for i in range(2, n):  # 1-indexed: positions 2..n-1
        if (x + a[i - 1]) % 2 == 1:
            ops.append((1, i))   # odd sum: a[i] := a[1] = x
        else:
            ops.append((i, n))   # even sum: a[i] := a[n] = x

    print(len(ops))
    for l, r in ops:
        print(l, r)

t = int(input())
for _ in range(t):
    solve()