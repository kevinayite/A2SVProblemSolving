t = int(input())
for _ in range(t):
    n = int(input())
    s = input().lower() 
    valid = True
    if s[0] != 'm':
        valid = False
    for i in range(1, n):
        previous = s[i-1]
        current = s[i]

        if current == previous:
            continue
        
        elif previous == 'm' and current == 'e':
            continue
        
        elif previous == 'e' and current == 'o':
            continue
        
        elif previous == 'o' and current == 'w':
            continue
        
        else:
            valid = False
            break
    if s[-1] != 'w':
        valid = False

    if valid:
        print("YES")
    else:
        print("NO")