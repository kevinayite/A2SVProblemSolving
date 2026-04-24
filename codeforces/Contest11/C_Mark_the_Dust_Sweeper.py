t = int(input())
for _ in range(t):
    n = int(input())
    dust = list(map(int, input().split()))
    start = 0
    while start < n and dust[start] == 0:
        start += 1
    
    total_operations = 0
    for i in range(start, n -1):
        if dust[i] == 0:
            total_operations += 1
        else:
            total_operations += dust[i]
    print(total_operations)
