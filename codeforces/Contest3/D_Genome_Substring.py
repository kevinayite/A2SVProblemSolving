n = int(input())
s = input()
target = "ACTG"
def dist(a,b):
    d = abs(ord(a)- ord(b)) # note that ord(a) != ord(A) here iti si doesn't matter as we are using uppercase letter
    return min(d, 26 - d)
answer = float('inf')
for i in range(n - 3):
    cost = 0
    for j in range(4):
        cost += dist(s[i + j], target[j]) # calculating the cost for each letter
    answer = min(answer, cost)
print(answer)