n, t = map(int, input().split())
arr = list(map(int, input().split()))
max_books = 0
left = 0
time_spend = 0
for right in range(n):
    time_spend += arr[right]
    while t < time_spend:
        time_spend -= arr[left]
        left +=1
    max_books = max(max_books, right - left +1)
print(max_books)
    
    