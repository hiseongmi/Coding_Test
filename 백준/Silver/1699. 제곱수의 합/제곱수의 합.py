n = int(input())

dp = [0] * (n+1)

for i in range(1, n+1): # 1 2 3 4 5 6 7 
    dp[i] = i # dp[10] = 10 /  dp[10-1] dp[9] = 1 더 작은 값을  
    for j in range(1, int(i**0.5)+1): # 1 2 3 4 5
        dp[i] = min(dp[i], dp[i - j*j]+1)
print(dp[n])