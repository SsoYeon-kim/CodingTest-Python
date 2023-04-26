'''
n = int(input())

flag = True
cnt = 1
while flag:
    if cnt == 1:
        start = 1
        end = 1
    else:
        start = end+1
        end = start + (cnt-1)*6 -1
    
    if n >= start and n <= end:
        print(cnt)
        break
    cnt += 1
'''

n= int(input())

beeHouse = 1
c = 1

while n>beeHouse:
    beeHouse += 6*c
    c += 1

print(c)

# 1 (1+6*0)
# 2 (1+(6*1))
# 3 (1+(6*2))