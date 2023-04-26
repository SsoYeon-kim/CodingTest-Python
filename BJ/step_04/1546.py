n = int(input())
score = list(map(int, input().split()))

max = max(score)
sum = 0

for s in score:
    new = s/max*100
    sum += new

print(sum/n)

