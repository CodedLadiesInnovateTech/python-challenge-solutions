'''4. Write a Python program to calculate the maximum profit from selling
 and buying values of stock. An array of numbers represent the stock prices in chronological order.
For example, given [8, 10, 7, 5, 7, 15], the function will return 10, since the buying value of the stock 
is 5 dollars and sell value is 15 dollars.
Sample Output:
10
7
0'''
def buy_and_sell(stock_price):
    max_profit_val, current_max_val = 0, 0 
    for price in reversed(stock_price):                       
        current_max_val = max(current_max_val, price)          
        potential_profit = current_max_val - price          
        max_profit_val = max(potential_profit, max_profit_val)

    return max_profit_val

print(buy_and_sell([8, 10, 7, 5, 7, 15]))
print(buy_and_sell([1, 2, 8, 1])) 
print(buy_and_sell([]))

#Reference: w3resource