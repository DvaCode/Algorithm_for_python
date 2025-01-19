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

def solution_11(s):
    """
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



