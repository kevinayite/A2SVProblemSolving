sound = input()
# print(sound)
n = int(input())
word= ""
sounds = []
for _ in range(n):
    son = input()
    sounds.append(son)
for i in sounds:
    word+=i
print(word)
if sound in word:
    print("YES")
else:
    print("NO")