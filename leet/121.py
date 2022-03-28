# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and 
# sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and 
# selling on day 1 is not allowed because you must buy before you sell.

prices = list(map(int, input().split()))

profit = 0
min_price = prices[0]
for i in prices:
    if i < min_price:
        min_price = i
    elif i - min_price > profit:
        profit = i - min_price

print(profit)