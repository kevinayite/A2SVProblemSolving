from collections import Counter
n = input()
n_dict = Counter(n)
x = str(n_dict['4'] + n_dict['7'])
if all(ch in {'4','7'} for ch in x):
    print("YES")
else:
    print("NO")