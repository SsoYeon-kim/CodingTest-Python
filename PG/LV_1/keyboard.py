def solution(keymap, targets):
    answer = []
    dic = dict()
    
    # O(mn) : m-keymap리스트 길이, n-각 문자열 길이
    for k in keymap:
        for i, c in enumerate(k):
            if c not in dic:
                dic[c] = i+1
            else:
                if dic[c] > i+1:
                    dic[c] = i+1
    
    # O(mn) : m-targets리스트 길이, n-각 문자열 길이
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


# O(mn) + O(mn) = O(2mn) = O(mn)
print(solution(["BC"], ["AC", "BC"]))