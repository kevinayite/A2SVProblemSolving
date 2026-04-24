t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = len(set(arr)) # amount of distinct number
    # k = number of suits up and k -1 = number of resets
    # result = k + k -1 = 2k -1
    print((2*k) -1)
    