n, s = map(int, input().split())
arr = list(map(int, input().split()))
l = 0
current_sum = 0
max_len = 0
for r in range(n):
    current_sum += arr[r]
    while current_sum > s:
        current_sum -= arr[l]
        l += 1
    max_len = max(max_len, r - l + 1)
print(max_len)