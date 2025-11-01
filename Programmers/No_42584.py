# 주식가격
def solution(prices):
    size_lst = len(prices)
    answer = [-1] * size_lst
    stack = []
    for i in range(size_lst):
        if not stack: # stack is empty
            stack.append(i)
        else: # Not empty  
            while stack and prices[stack[-1]]> prices[i]: # 주식 가격 하락한 경우
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            # 주식 가격 하락하지 않은 경우
            stack.append(i)
    if stack:
        stack=stack[::-1]
        for i in range(len(stack)):
            answer[stack[i]] = size_lst - stack[i] - 1

    return answer