n = int(input())
ans = list()

for i in range(n):
    ans.append(input())

for aa in ans:
    cnt = 0
    score = 0
    for a in aa:
        if a == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)