import sys
input = sys.stdin.readline

def sol():
    T = int(input())

    def DP(N):
        dp = [0] * max(4, N+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        if N < 4:
            return dp[N]
        for x in range(4, N+1):
            dp[x] = dp[x-1]+dp[x-2]+dp[x-3]
        return dp[N]

    for _ in range(T):
        n = int(input())
        print(DP(n))

sol()
