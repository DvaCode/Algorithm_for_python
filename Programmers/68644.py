# 두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    answer_list = []
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            if i != j:
                answer_list.append(numbers[i]+numbers[j])
    answer = list(set(answer_list))
    answer.sort()
    return answer