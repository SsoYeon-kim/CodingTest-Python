case = int(input())

for _ in range(case):
    score = list((map(int, input().split())))
    avg = sum(score[1:])/score[0]

    cnt = 0

    for i in score[1:]:
        if i > avg:
            cnt +=1
    ratio = cnt/score[0]*100
    print('%.3f'% ratio + '%')

