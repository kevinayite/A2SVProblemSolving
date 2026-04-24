from collections import Counter
def solve():
    t = int(input())
    for _ in range(t):
        
        n, k = map(int, input().split())
        s = input().strip()
        count = Counter(s)
        b = count['B']
        if b == k:
            print(0)
            continue # here use continue if u use return the remaining test won't be tested
        elif b < k:
            needed = k - b
            count_a = 0
            for i in range(len(s)):
                if s[i] == 'A':
                    count_a += 1
                if needed == count_a:
                    print( str(1)+ "\n" + str(i+1) + " B")
                    break
        else:
            needed = b - k
            count_b = 0
            for i in range(len(s)):
                if s[i] == 'B':
                    count_b += 1
                if needed == count_b:
                    print(str(1) + "\n" + str(i+1) + " A")
                    break
solve()



        


            
        

