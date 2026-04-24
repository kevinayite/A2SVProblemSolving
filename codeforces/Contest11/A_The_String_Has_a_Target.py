t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    result = min(s)
    last_index = s.rfind(result) # help us to find the last occurence
    #  of result here in our case, in case not found it will return -1 (for future uses)
    
    answer = result + s[:last_index] + s[last_index + 1 ::]
    print(answer)