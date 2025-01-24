# 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    stack_ = []
    size_ = len(board)
    board_ = []
    for idx_x in range(size_):
        lst = []
        for idx_y in range(size_ - 1, -1, -1):
            if board[idx_y][idx_x]:
                lst.append(board[idx_y][idx_x])
        board_.append(lst)
    for idx in moves:
        if board_[idx-1]:
            item = board_[idx - 1].pop()
            if stack_ and item == stack_[-1]:
                stack_.pop()
                answer += 2
            else:
                stack_.append(item)
    return answer