case = int(input())

for i in range(1, case+1):
    re, sentence = list(map(str, input().split()))
    re = int(re)

    for s in sentence:
        print(s*re, end='')
    print()