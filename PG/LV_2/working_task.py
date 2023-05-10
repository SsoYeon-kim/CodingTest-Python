def solution(plans):
    tasks = []
    answer = [] # [[과제명, 끝날시간]]

    # 시간 -> 분
    for plan in plans:
        tasks.append((plan[0], int(plan[1][:2])*60+int(plan[1][3:]), int(plan[2])))
    
    # 시작 시간이 빠른 순으로 정렬
    tasks = sorted(tasks, key=lambda x:x[1])

    for cls, start, time in tasks:
        # 이전 과제들이 끝날시간보다 현재 과제의 시작 시간이 빠르다면
        for i, cls_working in enumerate(answer):
            if cls_working[1] > start:
                # 이전 과제 끝날시간을 현재 과제의 러닝타임만큼 늦추기
                answer[i][1] += time
        # 과제명, 시작+러닝타임
        answer.append([cls, start+time])
    
    # 끝시간이 작은순으로 정렬한 후 과제명만 list로 
    answer = list(map(lambda x:x[0], sorted(answer, key=lambda x:x[1])))
    return answer

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# ["science", "history", "computer", "music"]
