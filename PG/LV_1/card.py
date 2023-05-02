from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    q1 = deque(cards1)
    q2 = deque(cards2)
    
    for g in goal:
        if q1 and g == q1[0]:
            q1.popleft()
        elif q2 and g == q2[0]:
            q2.popleft()
        else:
            return "No"
    answer = 'Yes'
    
    return answer
    
print(solution(	["i", "see", "to"], ["you", "now", "me"], ["i", "see", "now", "me"]))