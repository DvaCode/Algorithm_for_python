def solution(participant, completion):
    answer = ''
    hash_ = {}

    for i in participant:
        if i in hash_:
            hash_[i] += 1
        else:
            hash_[i] = 1
    
    for i in completion:
        hash_[i] -= 1
        if hash_[i] == 0:
            hash_.pop(i)
    key = list(hash_.keys())
    answer += str(key[0])
    
    return answer