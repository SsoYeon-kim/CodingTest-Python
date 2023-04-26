n = input()
cnt = 0

if len(n) == 1:
    n = '0' + n
num = n

while True:
    sum = str(int(num[0]) + int(num[1]))
    num = str(int(num[-1])) + sum[-1]
    cnt += 1

    if num == n:
        break

print(cnt)