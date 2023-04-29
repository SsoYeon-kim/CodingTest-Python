# def solution(players, callings):
#     answer = players[:]
#     for c in callings:
#         before_idx = answer.index(c)
#         answer[before_idx], answer[before_idx-1] = answer[before_idx-1], answer[before_idx]
#     return answer

# => .index로 players 배열의 처음부터 탐색

def solution(players, callings):
    dic = {p:i for i, p in enumerate(players)}
    
    for c in callings:
        before = dic[c]
        dic[players[before]] = before-1
        dic[players[before-1]] = before
        players[before], players[before-1] = players[before-1], players[before]
        
    return players

# => dict를 사용해 idx를 찾는 시간 단축
     
