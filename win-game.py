
# player 1 and 2 can add 1/2/5 stones in each round
# first to reach 100 stones win

def win(n):
	dp = [False] * (n+1)
	dp[1] = dp[2] = dp[5] = True
	for i in range(1, n+1):
		if dp[i] is True:
			continue
		for j in (i-1, i-2, i-5):
			if j >= 0:
				if dp[j] is False:
					dp[i] = True
					break
		else:
			dp[i] = False
	print(dp)
	return dp[-1]

inputs = [
	10, 30, 50, 100
]

for i in inputs:
	print(win(i))
