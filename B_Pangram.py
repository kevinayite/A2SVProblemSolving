n = int(input())
word = input()
word = word.upper()
alphabet_set = {'A', 'B', 'C', 'D', 'E', 'F',
 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
  'W', 'X', 'Y', 'Z'}
if n >= 26 and (set(word) >= alphabet_set):
    print("YES")
else:
    print("NO")