number_test_cases = int(input())
for _ in range(number_test_cases):
    n, k = map(int, input().split())
    brand_sum = [0]*(k+1) # we define lenght of k+1 as 1≤bi≤k 
    used = []
    for i in range(k):
        b, c = map(int, input().split())
        if brand_sum[b] == 0:
            used.append(b)
        brand_sum[b] += c
    values = [brand_sum[b] for b in used]
    values.sort(reverse= True)
    print(sum(values[:n]))