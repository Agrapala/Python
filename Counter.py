from collections import Counter

# Input
X = int(input())  # Number of shoes
shoe_sizes = list(map(int, input().split()))
N = int(input())  # Number of customers

# Create a counter for available shoe sizes
inventory = Counter(shoe_sizes)
total_money = 0

# Process each customer
for _ in range(N):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        total_money += price
        inventory[size] -= 1

# Output the total earnings
print(total_money)
