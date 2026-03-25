t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    a = [] # let us obtain our grid first
    for _ in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    if n * m == 1:
        print(-1)
        continue # goes to the next test case
    flat_a = []
    for i in range(n):
        for j in range(m):
            flat_a.append(a[i][j]) # here at the end we have a 1D array
    rotated = [flat_a[-1]]  + flat_a[:-1] # creating a array with the first index with the last one
    idx = 0 # use to traverse our rotated array
    b = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(rotated[idx])
            idx +=1
        b.append(row)
    # printing the result 
    for row in b:
        print(*row)
