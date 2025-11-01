# 표 편집
def solution(n, k, cmd):
    # prev[i]: i의 바로 '위' 행, next[i]: i의 바로 '아래' 행
    stack = []
    table = ['O'] * n
    up = [ i - 1 for i in range(n)]
    up[0] = -1
    down = [i + 1 for i in range(n)]
    down[n - 1] = -1
    for item in cmd:
        X = 0
        target = 0
        # input Part
        cmd_word = item.split()
        if len(cmd_word) > 1:
            cmd_ , X = cmd_word[0], int(cmd_word[1])
        else:
            cmd_ = cmd_word[0]
        # print(cmd_, X, k)
        # Operation Part
        if cmd_ == 'U':
            # X만큼 위로 Selected 행을 변경
            for _ in range(X):
                k = up[k]
        elif cmd_ == 'D':
            # X만큼 아래로 Selected 행을 변경
            for _ in range(X):
                k = down[k]
        elif cmd_ == 'C':
            # 현재 선택된 행을 삭제, 바로 아래 행 선택
            # 삭제된 행이 맨 마지막인 경우 바로 윗 행 선택
            # 삭제 하기 전에 현재 선택된 행이 맨 마지막인지 아닌지 판단
            stack.append(k)
            table[k] = 'X'
            if down[k] != -1: up[down[k]] = up[k]
            if up[k] != -1: down[up[k]] = down[k]
            k = up[k] if down[k] == -1 else down[k]
        else:# cmd == 'Z택
            recover_idx = stack.pop()
            table[recover_idx] = 'O'
            # 윗 행, 아래 행 인지 경계 검사 처리
            if up[recover_idx] != -1: down[up[recover_idx]] = recover_idx
            if down[recover_idx] != -1: up[down[recover_idx]] = recover_idx
    answer=''
    for item in table:
        answer += item
    return answer
