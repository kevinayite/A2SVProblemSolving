k,n,w = map(int, input().split())
somme = 0
for w in range(1, w+1):
    somme += w*k
if n>= somme: 
    print(0)
else:
    print(somme-n)

