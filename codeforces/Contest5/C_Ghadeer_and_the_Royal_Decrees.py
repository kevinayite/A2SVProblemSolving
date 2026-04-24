t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    maximum = 0
    maximum = max(arr)
    result = []
    for i in range(m):
        c, l , r = input().split()
        l = int(l)
        r = int(r)
        if maximum >= l and maximum <= r:
            if c == '+':
                maximum += 1
            else:
                maximum -= 1
            
        result.append(maximum)
    print(*result)



