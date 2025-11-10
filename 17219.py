import sys
from collections import defaultdict

input = sys.stdin.readline

def sol():
    website_pw = defaultdict(list)
# input part
    N, M = map(int, input().split())
    for _ in range(N):
        website, pw = input().split()
        website_pw[website] = pw

    for _ in range(M):
        quest = input().rstrip("\n")
        print(website_pw[quest])
    print(website_pw)
sol()
