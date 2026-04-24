password = input().strip()
n = int(input())

a, b = password[0], password[1]

end_with_a = False
start_with_b = False
for _ in range(n):
    w = input().strip()

    if w == password:
        print("YES")
        exit()

    if w[1] == a:
        end_with_a = True

    if w[0] == b:
        start_with_b = True
if end_with_a and start_with_b:
    print("YES")
else:
    print("NO")