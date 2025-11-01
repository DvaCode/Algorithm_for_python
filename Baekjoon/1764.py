import sys

input = sys.stdin.readline

def sol():
    N, M = map(int, input().split())
    n = set()
    m = set()
    for _ in range(N):
        str = input().rstrip('\n')
        n.add(str)
    
    for _ in range(M):
        str = input().rstrip('\n')
        m.add(str)
    
    ans = n & m
    # print(ans)
    print(len(ans))
    for i in sorted(ans):
        print(i)

sol()