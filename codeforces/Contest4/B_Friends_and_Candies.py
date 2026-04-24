t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    if total % n !=0:
        print(-1)
        continue
    else:
        average = total // n
        result = 0
        for a in arr:
            if a > average:
                result += 1
        print(result)

    
    