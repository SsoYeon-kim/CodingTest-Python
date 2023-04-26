# n1, n2 = input().split()
# num1 = list(map(int, str(n1)))
# num2 = list(map(int, str(n2)))

# tmp = ''
# tmp = num1[0]
# num1[0] = num1[-1]
# num1[-1] = tmp

# tmp = num2[0]
# num2[0] = num2[-1]
# num2[-1] = tmp

# a = ''
# b = ''

# for n in num1:
#     a += str(n)
# for n in num2:
#     b += str(n)
# if int(a) > int(b):
#     print(a)
# else:
#     print(b)

num1, num2 = input().split()
num1 = int(num1[::-1])
num2 = int(num2[::-1])

if num1 > num2 :
    print(num1)
else:
    print(num2)