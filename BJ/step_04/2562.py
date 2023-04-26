'''
num = list()

for i in range(9):
    num.append(int(input()))

max = num[0]

for i, n in enumerate(num):
    if n > max:
        max = n
        max_index = i+1

print(max)
print(max_index)
'''

num = list()
for i in range(9):
    num.append(int(input()))

print(max(num))
print(num.index(max(num))+1)
