case = int(input())
num = input()

nums = list(map(int, str(num)))

sum = 0

for n in nums:
    sum += n

print(sum)