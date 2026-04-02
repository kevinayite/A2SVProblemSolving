t = int(input())
for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if max(x1, y1) <= min(x2, y2):
        print("NO")
    else:
        print("YES")
