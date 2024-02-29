from typing import List


def get_maximum_amount_of_gold(mines):
    n = len(mines)
    if n == 0:
        return 0
    
    m = len(mines[0])

    if m == 0:
        return 0
    
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = mines[i][0]

    for j in range(1, m):
        for i in range(n):
            left = dp[i][j - 1]
            upper_left = dp[i - 1][j - 1] if i > 0 else 0
            dp[i][j] = mines[i][j] + max(left, upper_left)

    return max(dp[i][m - 1] for i in range(n))
