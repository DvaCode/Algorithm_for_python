import sys
input = sys.stdin.readline

def sol():
    N = int(input())

    def DP(N):
        dp = [0] * ( N + 1 )
        dp[1] = 0
        for target in range(2, N+1):
            MIN = dp[target - 1] + 1
            if target % 2 == 0:
                MIN = min(MIN, dp[target // 2 ] + 1)
            if target % 3 == 0:
                MIN = min(MIN, dp[target // 3] + 1)
            dp[target] = MIN

        return dp[N]
    print(DP(N))

sol()
