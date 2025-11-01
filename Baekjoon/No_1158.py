# 1158.py
# Baekjoon Problem No.1158 요세푸스

from collections import deque

def mistfit_sol(N,K):
    # deque로 queue 사용
    queue = [i for i in range(1,N+1)]
    result = []
    item = 0
    # idx = 인덱싱 할 변수

    while queue:
        if K < len(queue):
            # queue 재조정
            # queue = queue[K+1:] + queue[:K]
            # item = queue.leftpop
            # result.append(item)
            queue = queue[K - 1: ] + queue[:K - 1]
            item = queue.pop(0)
            result.append(item)
        else: # K >= len(queue):
            # idx = K - len(queue)
            # queue = queue[idx+1:] + queue[:idx]
            # item = queue.leftpop
            # result.append(item)
            # 이 코드의 문제점
            # K > len(queue)가 되었을 경음
            # idx > len(queue) 인 경우 queue lst 슬라이스 할때 idx는 queue의 out of index arrange가 되어서
            # queue 회전연산이 정상적으로 수행되지 않음
            idx = K - len(queue)
            queue = queue[idx - 1:] + queue[:idx - 1]
            item = queue.pop(0)
            result.append(item)
    return result

def sol(N, K):
    queue = [i for i in range(1,N+1)]
    result = []
    item = 0

    while queue:
        idx = (K - 1) % len(queue)
        queue = queue[ idx : ] + queue[ : idx ]
        item = queue.pop(0)
        result.append(item)

    return result

def sol_2(N,K):
    queue = list(range(1,N+1))
    result = []
    idx = 0

    while queue:
        # 현재 남은 인원의 길이에 대해 (k - 1)를 더한 후 나머지 연산 수행
        idx = ( idx + K - 1) % len(queue)
        result.append(queue.pop(idx))
    return result