n = int(input())
num = list(map(int, input().split()))

min = num[0]
max = num[0]

for i in num:
    if i < min:
        min = i
    elif i > max:
        max = i

print(min, max)