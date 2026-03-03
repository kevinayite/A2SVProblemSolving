from collections import Counter
result = "NO"
number_days = int(input())
all_entries = []

for _ in range(number_days):
    number_test_cases = int(input()) 
    
    for _ in range(number_test_cases):
        name, value = input().split()
        all_entries.append((name, int(value)))

counter = Counter(all_entries)
for value in counter.values():
    if value >= 0.8 * number_days:
        result = "YES"
        break

print(result)