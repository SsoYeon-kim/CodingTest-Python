def solution(keymap, targets):
    answer = []
    dic = dict()
    for k in keymap:
        for i, c in enumerate(k):
            if c not in dic:
                dic[c] = i+1
            else:
                if dic[c] > i+1:
                    dic[c] = i+1
    
    for ta in targets:
        cnt = 0
        for t in ta:
            if t not in dic:
                cnt = -1
                break
            else:
                cnt += dic[t]
        answer.append(cnt)

    return answer

print(solution(["BC"], ["AC", "BC"]))