from collections import Counter
t = int(input())
for _ in range(t):
    s = input().strip()
    freq = Counter(s)
    start = 0
    for char in s:
        if freq[char] > 1:
            freq[char] -= 1
            start += 1
        else:
            break
    print(s[start:])

