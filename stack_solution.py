stack = []
max_size = 10

def isFull(stack):
    # 스택이 가득 찼는지 확인하는 함수
    return len(stack) == max_size

def isEmpty(stack):
    # 스택이 비어 있는지 확인하는 함수
    return len(stack) == 0

def push(stack, item):
    # 스택에 데이터를 추가하는 함수
    if isFull(stack):
        print("스택이 가득 찼습니다.")
    else:
        stack.append(item)
        print("데이터가 추가되었습니다.")

def pop(stack):
    # 스택에서 데이터를 꺼내는 함수
    if isEmpty(stack):
        print("스택이 비어 있습니다.")
        return None
    else:
        return stack.pop()

def solution(s):
    # 괄호 짝 맞추기
    answer = 0
    for i in s:
        if i == '(' :
            answer += 1
        elif i == ')':
            answer -= 1
        if answer < 0:
            print('False')
            return
    if answer == 0: print('True')
    else: print('False')

def solution_8(s):
    # chapter 6 문제 8
    stack_lst = []
    for c in s:
        if c == '(':
            stack_lst.append(c)
        elif c== ')':
            if not stack:
                return False
            else:
                stack_lst.pop()
    if stack:
        return False
    else:
        return True

def solution_9(decimal):
    # 10진수를 2진수로 변환하기
    stack = []
    answer = ''
    while decimal > 0:
        remainder = decimal % 2
        decimal //= 2
        stack.append(str(remainder))
    return (answer.join(stack[::-1]))

def solution_10_1(s):
    answer = 0
    open_ = ['(', '{', '[']
    close_ = [')', '}', ']']
    # 매번 왼쪽으로 회전하는 로직
    for i in range(0, len(s)):
        temp_s = s[i:] + s[:i]
        # 올바른 괄호인지 검증하는 로직
        stack = []
        for char_s in temp_s:
            if char_s in open_:
                stack.append(char_s)
            else:
                if not stack: break # stack is empty break

            for i in range(3):
                if char_s == close_[i] and stack[-1] == open_[i]:
                    stack.pop()

        else:
            if not stack:
                answer += 1
    return answer

def solution_10_2(s):
    answer = 0
    # 매번 왼쪽으로 회전하는 로직
    for i in range(0, len(s)):
        temp_s = s[i:] + s[:i]
        # 올바른 괄호인지 검증하는 로직
        if sol(temp_s) == True:
            answer += 1
    return answer

def sol(s):
    # 올바른 괄호인지 검사하는 함수
    stack = []
    open_ = {'(' : ')', '{' : '}', '[' : ']'}
    for char in s:
        if char in open_:
            stack.append(char)
        elif char in open_.values():
            if not stack or open_[stack.pop()] != char:
                return False
    return not stack

def rotate_left(s, n):
    """
    문자열 s를 왼쪽으로 n번 회전시킵니다.

    Parameters:
    s (str): 회전할 문자열
    n (int): 회전할 횟수

    Returns:
    str: 왼쪽으로 n번 회전된 문자열
    """
    n = n % len(s)  # n이 문자열 길이보다 클 경우를 대비
    return s[n:] + s[:n]


def rotate_right(s, n):
    """
    문자열 s를 오른쪽으로 n번 회전시킵니다.

    Parameters:
    s (str): 회전할 문자열
    n (int): 회전할 횟수

    Returns:
    str: 오른쪽으로 n번 회전된 문자열
    """
    n = n % len(s)  # n이 문자열 길이보다 클 경우를 대비
    return s[-n:] + s[:-n]

def solution_11_1(s):
    """
    오답 코드
    1. 알파벳 소문자로 구성된 문자열 s에서 같은 알파벳 2개 붙어 있는 짝을 찾음
    2. 그 짝을 제거함
    3. 앞뒤로 문자열을 이어붙임
    4. 1 ~ 3을 반복해서 문자열을 모두 제거하면 종료하는데 가능하면 1 리턴, 아니면 0 리턴
    :param s:
    :return:
    """
    answer = 0
    stack = []
    temp_str = s
    if len(s) % 2 != 0: return 0 # 문자열 길이가 홀수면 불가능
    while temp_str:
        for i in range(len(temp_str)):
            char_ = temp_str[i]
            if not stack:
                stack.append(char_)
            # 문자열에서 짝 탐색
            elif stack:
                if char_ == stack[-1]:
                    # 문자열에서 같은 알파벳 2개 붙어있는 부분 찾음
                    temp_str = temp_str[:i-1] + temp_str[i+1:] # str 에서 삭제 연산하고 난 이후 temp_str 재정의
                    stack = [] # 스택 초기화
                    break # for loop escape
                    # stack.append(char_) 삽입 연산 안 함
                else:
                    # 같지 않은 경우
                    stack.append(char_)
        else:
            return 0
    return 1

def solution_11_2(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return int(not stack)

def solution12_1(prices):
    size_lst = len(prices)
    answer = [-1] * size_lst
    stack = []
    for i in range(size_lst):
        if not stack: # stack is empty
            stack.append(i)
        else: # Not empty
            if prices[stack[-1]]> prices[i]: # 주식 가격 하락한 경우
                while True:
                    answer[stack[-1]] = i - stack[-1]
                    stack.pop()
                    if prices[stack[-1]] <= prices[i]:
                        
                        stack.append(i)
                        break
            else: # 주식 가격 하락하지 않은 경우
                stack.append(i)
    if stack:
        stack=stack[::-1]
        for i in range(len(stack)):
            answer[stack[i]] = size_lst - stack[i] - 1

    return answer

def solution12_1_2(prices):
    size_lst = len(prices)
    answer = [-1] * size_lst
    stack = []
    for i in range(size_lst): # 주식 가격 하락한 경우
        while stack and prices[stack[-1]] > prices[i]: # if stack: while 조건문 : 이렇게 하면 런타임이 발생함
            answer[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    if stack:
        stack=stack[::-1]
        for i in range(len(stack)):
            answer[stack[i]] = size_lst - stack[i] - 1

    return answer

def solution12_2(prices):
    n = len(prices)
    answer = [0] * n
    stack = [0]
    for i in range(1,n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    return answer


def solution13_1(board, moves):
    #loop mv_idx in moves:
        # 보드 판 제거 연산 if item != 0 이면 연산 수행
            # if stack_ and stack_[-1] == item:
                # stack_.pop()
                # answer += 1
            # stack_append(item)
    '''
    board = 현재 인형뽑기 보드 판
    moves = 크레인 작동할 위치
    answer = 터트러져서 사라진 인형의 개수
    1. 해당되는 격자로 이동
        1-1 인형있는지 검사
            1-1-1 있으면 pop
            1-1-2 없으면 skip
        1-2 없으면 skip
    
    '''
    answer = 0
    stack_ = []
    item = 0
    size_ = len(board)
    board_ = []
    for idx_x in range(size_):
        lst = []
        for idx_y in range(size_ - 1, -1, -1):
            if board[idx_y][idx_x] != 0:
                lst.append(board[idx_y][idx_x])
        board_.append(lst)
    print(board_)
    for idx in moves:
        print("stack : ", stack_)
        if board_[idx-1]: item = board_[idx - 1].pop()
        cnt = 0
        while stack_ and stack_[-1] == item:
            print("item: ",item, " stack : ", stack_)
            stack_.pop()
            cnt += 1
        if cnt != 0: answer += cnt + 1
        if stack_ and stack_[-1] != item: stack_.append(item)
        elif not stack_ : stack_.append(item)
    return answer

def solution13_(board, moves):
    #loop mv_idx in moves:
        # 보드 판 제거 연산 if item != 0 이면 연산 수행
            # if stack_ and stack_[-1] == item:
                # stack_.pop()
                # answer += 1
            # stack_append(item)
    '''
    board = 현재 인형뽑기 보드 판
    moves = 크레인 작동할 위치
    answer = 터트러져서 사라진 인형의 개수
    1. 해당되는 격자로 이동
        1-1 인형있는지 검사
            1-1-1 있으면 pop
            1-1-2 없으면 skip
        1-2 없으면 skip
    
    '''
    answer = 0
    stack_ = []
    item = 0
    size_ = len(board)
    board_ = []
    for idx_x in range(size_):
        lst = []
        for idx_y in range(size_ - 1, -1, -1):
            if board[idx_y][idx_x] != 0:
                lst.append(board[idx_y][idx_x])
        board_.append(lst)
    print(board_)
    for idx in moves:
        cnt = 0
        item = 0
        stack_idx = -1
        if board_[idx-1]:
            item = board_[idx - 1].pop()
            stack_.append(item)
        print("post_stack : ", stack_)
        while stack_ and len(stack_) > 1 and stack_[stack_idx] == item:
            #item = stack_.pop()
            cnt += 1
            if stack_[stack_idx - 1]:
                stack_idx -= 1
            else: break
        if cnt > 1:
            for _ in range(cnt):
                stack_.pop()
            answer += cnt
        print("item: ",item, " stack : ", stack_)
        print(answer) 
    print('final stack ->', stack_)
    return answer

def solution13_2(board, moves):
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

def solution14_(n,k,cmd):
    '''
    n = 행 개수
    k = 처음 선택된 행의 위치
    cmd = 명령어
    '''
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
            print('U : up list ->',up)
            for _ in range(X):
                print('U, k, up[k]',k,up[k])
                k = up[k]
            print('cmd : U, k : ', k)
        elif cmd_ == 'D':
            # X만큼 아래로 Selected 행을 변경
            for _ in range(X):
                k = down[k]
            print('cmd : D, k : ', k)
        elif cmd_ == 'C':
            # 현재 선택된 행을 삭제, 바로 아래 행 선택
            # 삭제된 행이 맨 마지막인 경우 바로 윗 행 선택
            # 삭제 하기 전에 현재 선택된 행이 맨 마지막인지 아닌지 판단
            stack.append(k)
            table[k] = 'X'
            if up[k] != -1: up[down[k]] = up[k]
            if down[k] != -1: down[up[k]] = down[k]
            k = up[k] if down[k] == -1 else down[k]
            print('C : up list ->',up)
            print('C : down list ->',down)
            print('k : ', k)
        else:# cmd == 'Z'
            recover_idx = stack.pop()
            table[recover_idx] = 'O'
            if up[recover_idx] != -1: down[up[recover_idx]] = recover_idx
            if down[recover_idx] != -1: up[down[recover_idx]] = recover_idx
            print('Z : up list ->',up)
            print('Z : down list ->',down)
            print('k : ', k)
    answer=''
    for item in table:
        answer += item
    return answer

def solution14_1(n,k,cmd):
    deleted = []
    up_lst = [i - 1 for i in range(n + 2)]
    down_lst = [i + 1 for i in range(n + 1)]
    k += 1
    for cmd_item in cmd:
        if cmd_item.startswith('C'):
            deleted.append(k)
            up_lst[down_lst[k]] = up_lst[k]
            down_lst[up_lst[k]] = down_lst[k]
            k = up_lst[k] if n < down_lst[k] else down_lst[k]
        elif cmd_item.startswith('Z'):
            restore = deleted.pop()
            down_lst[up_lst[restore]] = restore
            up_lst[down_lst[restore]] = restore
        else:
            if cmd_item.startswith('U'):
                for _ in range(int(cmd_item[2])):
                    k = up_lst[k]
            else:
                for _ in range(int(cmd_item[2])):
                    k = down_lst[k]
    answer = ['O'] * n
    for i in deleted:
        answer[i - 1] = 'X'
    return ''.join(answer)