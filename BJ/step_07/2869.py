'''
# 시간 초과!

a, b, v = map(int, input().split())
cnt = 0
move = 0
while True:
    cnt += 1
    move += a
    if move >= v:
        break
    else:
        move -= b
        if move >= v:
            break
print(cnt)
'''

import sys
import math

a, b, v = map(int, sys.stdin.readline().split())
move = math.ceil((v-b)/(a-b))

print(move)

# 올라가는 횟수 : x
# 내려오는 횟수 : x-1
# ax - b(x-1) = v
# x = (v-b)(a-b)