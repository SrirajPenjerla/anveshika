def max_common_subsequence(s1, s2, k):
    n, m = len(s1), len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    max_len = dp[n][m]

    for i in range(n):
        for j in range(m):
            for p in range(k + 1):
                if i + p < n and j + p < m and s1[i] == s2[j]:
                    dp[i + p + 1][j + p + 1] = max(dp[i + p + 1][j + p + 1], dp[i][j] + p + 1)

    return max_len


# Input
s1 = input().strip()
s2 = input().strip()
k = int(input().strip())

# Output
result = max_common_subsequence(s1, s2, k)
print(result)
