prices = [29.99, 45.50, 12.75, 38.20]
discount = [0.1, 0.2, 0.15, 0.05]
for price in range(len(prices)):
    prices[price] = prices[price] * (1 - discount[price])
    print(f"Updated price for item {price}: ${prices[price]:.2f}")