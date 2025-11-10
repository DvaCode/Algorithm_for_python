import sys

input = sys.stdin.readline

def sol():
    N = int(input())
    meetings = []
    # lst = [ (start, end, dist)]
    # sort first start point, and then sort dist at the point
    for _ in range(N):
        a, b = map(int, input().split())
        meetings.append((a,b)) # a is start, b is end, b - a = distance
    # sort part
    meetings.sort(key=lambda x : (x[1], x[0]))
    # print(meetings)
    end = 0
    ans = 0
    for s_, e_ in meetings:
        if s_ >= end:
            end = e_
            ans += 1
    print(ans)
sol()
