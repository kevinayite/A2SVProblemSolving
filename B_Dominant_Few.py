number_test_cases = int(input())
for _ in range(number_test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    x = n//2 + 1
    if sum(arr[:x]) >= sum(arr[x:]):
        print("NO")
    else:
        print("YES")
    

