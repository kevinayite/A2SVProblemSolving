n = int(input())
arr = list(map(int, input().split()))
even = False
odd = False

for number in arr:
    if number % 2 == 0:
        even = True
    else:
        odd = True
if even and odd:
    arr.sort()
print(*arr)