num = list(map(int, input().split()))

def solve(num:list):
    # sum = 0
    # for n in num:
    #     sum += n
    return sum(num)

print(solve(num))