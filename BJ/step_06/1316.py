'''
case = int(input())
cnt = 0
flag = True

for i in range(case):
    sentence = list(map(str, input()))
    group = list()
    group.append(sentence[0])
    for s in sentence:
        flag = True
        if s != group[-1] and s not in group:
            group.append(s)
        elif s != group[-1] and s in group:
            flag = False
            group = []
            sentence = []
            break

    
    if flag:
        if len(group) == len(set(sentence)):
            cnt += 1
            group = []
            sentence = []

print(cnt)
'''

case = int(input())
cnt = case

for i in range(case):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)