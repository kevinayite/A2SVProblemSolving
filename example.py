words = ["Hello","Alaska","Dad","Peace"]
result = []
for word in words: 
    if set(word)<=set("qwertyuiop") or set(word)<=set("asdfghjkl") or set(word)<=set("zxcvbnm"):
        result.append(word)
        print(result)
print(result)