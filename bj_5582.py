first = input()
second = input()
max_len = 0
dp = [[0 for j in range(len(second)+1)] for i in range(len(first)+1)]
# print(first)
# print(second)
for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        if first[i-1] == second[j-1]:
            if first[i-1] == second[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len: max_len = dp[i][j]
                
        
print(max_len)