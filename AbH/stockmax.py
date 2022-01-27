from queue import Queue
import copy
#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#
def computeProfit(currItem, stocks):
    #print("Called")
    curr_stocks = copy.deepcopy(stocks)
    cost_incurred = 0
    size = len(curr_stocks)
    curr_profit = 0
    new_stocks = []
    while(size>0):
        price = curr_stocks.pop()
        #print(price)
        cost_incurred+=price
        if(currItem > price):
            curr_profit+=currItem
        else:
            new_stocks.append(price)
            
        size-=1

    #print("Came out!")
        
    return curr_profit-cost_incurred, new_stocks
        
def solveRecursive(prices, stocks, profit):
    print("Prices right now {}".format(prices))
    print("Stocks right now {}".format(stocks))
    print("Profit right now {}".format(profit))
    if(len(prices) == 0):
        #print("OK")
        return profit

    
    stocks.append(prices[0])
    profit = solveRecursive(prices[1:], stocks, profit)
    stocks.pop()

    if(len(stocks) != 0):
        computed_profit, cmp_stocks = computeProfit(prices[0], stocks)
        
        if(computed_profit>0):
            profit += computed_profit
            profit = solveRecursive(prices[1:], cmp_stocks, profit)
        

    profit = solveRecursive(prices[1:], stocks, profit)
    
    return profit
    
        
        
def stockmax(prices):
    # Write your code here
    stocks = []
    profit = solveRecursive(prices, stocks, 0)
    return profit

print(stockmax([1,3,1,2]))