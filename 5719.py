import sys
import heapq
from collections import defaultdict

INF = float("inf")
input = sys.stdin.readline

def sol():
    while True:

        N, M = map(int, input().split())
        if N != 0 and M != 0:
            S, D = map(int, input().split())
            graph = defaultdict(list)

            for _ in range(M):
                U, V, P = map(int, input().split())
                graph[U].append((V,P))
