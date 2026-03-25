import sys 

read_input = sys.stdin.readline

num_products = int(read_input())
products = []

for _ in range(num_products):
    required_amount, discount_threshold = map(int, read_input().split())
    products.append([required_amount, discount_threshold])
    
# Trier par seuil de réduction (b_i)
products.sort(key=lambda product: product[1])

left_index = 0
right_index = num_products - 1

total_cost = 0
total_bought = 0

while left_index <= right_index:
    required_amount, discount_threshold = products[left_index]
    
    if discount_threshold <= total_bought:
        # On peut acheter à prix réduit (1 ruble)
        total_bought += required_amount
        total_cost += required_amount
        left_index += 1
    else:
        # On doit acheter à prix plein (2 rubles)
        needed_to_unlock = discount_threshold - total_bought
        available_amount = products[right_index][0]
        
        amount_to_buy = min(needed_to_unlock, available_amount)
        
        total_bought += amount_to_buy
        total_cost += 2 * amount_to_buy
        
        products[right_index][0] -= amount_to_buy
        
        if products[right_index][0] == 0:
            right_index -= 1
            
print(total_cost)