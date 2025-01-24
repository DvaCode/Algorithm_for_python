# 괄호 회전하기
def solution(s):
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