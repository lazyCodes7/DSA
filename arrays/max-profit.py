def maxProfit(prices, n):
	profit = [0]*n
	max_price = 0
	for i in range(n-2,0,-1):
		if(prices[i]>max_price):
			max_price = prices[i]

		profit[i] = max(profit[i+1],max_price-prices[i])

	min_price = prices[0]


	for j in range(1,n):
		if(min_price>prices[j]):
			min_price = prices[j]

		profit[j] = max(profit[j-1], prices[j]-min_price)

	return profit[n-1]

print(maxProfit([5,4,3,2,1],5))


