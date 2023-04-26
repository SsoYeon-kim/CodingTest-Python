num = list()
res = set()

for i in range(10):
    num.append(int(input()))

for n in num:
    res.add(n%42)
print(len(res))

