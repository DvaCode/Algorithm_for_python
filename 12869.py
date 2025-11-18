import sys
from collections import deque

input = sys.stdin.readline

def sol():
    N = int(input())
    input_val = [ input().split() ]
    scv = [] * N
    for idx in range(N):
        scv[idx] = input_val[idx]
