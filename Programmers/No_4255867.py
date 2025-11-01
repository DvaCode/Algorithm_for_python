import math

def solution(progresses, speeds):
    answer = []
    size_ = len(progresses)
    deploy = [-1] * size_
    
    for i in range(size_):
        deploy[i] = math.ceil((100 - progresses[i]) / speeds[i])
    init = deploy[0]
    count = 0
    
    if size_ != 1:
        for i in range(size_):
            if init < deploy[i]:
                init = deploy[i]
                # 크다면 비교 기준 변수 값 갱신
                # answer에 현재 배포 개수 추가하고 count = 0
                
                answer.append(count)
                count = 1
            elif init >= deploy[i]:
                count += 1
            if i == size_ - 1:
                answer.append(count)
    else:
        answer.append(1)            
    return answer