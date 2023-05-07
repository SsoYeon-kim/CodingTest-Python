def solution(book_time):
    dic = dict()
    
    for time in book_time:
        # 분으로 바꾸기
        start = int(time[0][:2]) * 60 + int(time[0][3:])
        end = int(time[1][:2]) * 60 + int(time[1][3:]) + 10

        # 930 퇴실일 경우 (for문은 929까지이므로 930 입실 가능)
        for i in range(start, end):
            if dic.get(i) == None:
                dic[i] = 1
            else:
                dic[i] += 1
    
    return max(dic.values())

print(solution([["09:00","09:20"], ["09:10","09:40"],["09:30","10:10"]]))
