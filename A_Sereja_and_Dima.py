n = int(input())
arr = list(map(int, input().split()))

left, right = 0, n-1
sum_sereja, sum_dima = 0, 0

for i in range(n):
    if arr[left] > arr[right]:
        picked_number = arr[left]
        left +=1
    else:
        picked_number = arr[right]
        right -=1
    if i % 2 == 0:
        sum_sereja += picked_number
    else:
        sum_dima += picked_number

print(sum_sereja, sum_dima)
