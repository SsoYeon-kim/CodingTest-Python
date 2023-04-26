num = input()

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for n in num:
    for d in dial:
        if n in d:
            time += dial.index(d)+3

print(time)