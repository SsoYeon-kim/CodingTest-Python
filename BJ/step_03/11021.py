import sys

case = int(input())

for i in range(1,case+1):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #'+str(i)+': '+ str(a+b))