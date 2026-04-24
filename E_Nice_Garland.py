n = int(input())
s = input().strip()

r = [0,0,0]
g = [0,0,0]
b = [0,0,0]

for i in range(0, len(s), 3):
    if s[i]!= "R":
        r[0] += 1
    if s[i] != "G":
        g[0] += 1
    if s[i] != "B":
        b[0] += 1
    
    if i + 1 < n:
        if s[i + 1] != "R":
            r[1] += 1
        if s[i + 1] != "G":
            g[1] += 1
        if s[i + 1] != "B":
            b[1] += 1
    if i + 2 < n:
        if s[i + 2] != "R":
            r[2] += 1
        if s[i + 2] != "G":
            g[2] += 1
        if s[i + 2] != "B":
            b[2] += 1

res = {
    r[0] + g[1] + b[2]: "RGB",
    r[0] + b[1] + g[2]: "RBG", 
    b[0] + r[1] + g[2]: "BRG", 
    b[0] + g[1] + r[2]: "BGR", 
    g[0] + r[1] + b[2]: "GRB", 
    g[0] + b[1] + r[2]: "GBR"
}
mini = min(res) # taking the minimum among the  keys

rem = n % 3
lights = res[mini] * (n // 3) + res[mini][:rem]
print(mini)
print(lights)
