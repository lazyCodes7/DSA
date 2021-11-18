import sys
def coinchange(coins, m, change, memo = {}):
	minchange = sys.maxsize
	if(change in memo.keys()):
		return memo[change]
	if(change == 0):
		return 0

	else:
		for i in range(m):
			if(coins[i]<=change):
				result = coinchange(coins, m, change-coins[i], memo)
				if(result != sys.maxsize and result<minchange):
					minchange = result+1

		memo[change] = minchange
		return memo[change]

def solve():
	coins = [9,3,6,9]
	change = 11
	m = len(coins)

	result = coinchange(coins, m, change)
	if(result == sys.maxsize):
		return -1

	else:
		return result
print(solve())
