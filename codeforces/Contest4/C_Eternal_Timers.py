t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    possible = True
    for i in range(n):
        maxDistance = max(i, n - i - 1)
        if arr[i] <= 2 * maxDistance: # we won't be able to come back
            possible = False 
            break
    if possible:
        print("YES")
    else:
        print("NO")