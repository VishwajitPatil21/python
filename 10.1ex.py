# Price Engine

costs = [1250.50, 4500.75, 2300.25, 7800.90, 3200.40, 950.00]

# Sort from highest to lowest
costs.sort(reverse=True)

# Display top three priciest assets
print("Top 3 Priciest Assets:")

for i in range(min(3, len(costs))):
    print(f"{i + 1}. ₹{costs[i]:.2f}")