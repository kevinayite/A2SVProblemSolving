t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0
    for i in range(1, n):
        # logic behind
        # Are there enough numbers with larger absolute values than a1
        #  so we can move them around and place a1 in the middle?
        if abs(arr[i]) < abs(arr[0]):
            count += 1
    median_position = (n + 1) // 2
    if median_position <= n - count:
        print("YES")
    else:
        print("NO")