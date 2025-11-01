def solution42993(skill, skill_trees):
    answer = 0
    for idx in skill_trees:
        stack = list(skill)
        for item in idx:
            if stack[0] == item:
                stack.pop(0)
        if not stack:
            answer += 1
    return answer