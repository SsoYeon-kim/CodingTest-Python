n = int(input())

def han(num):
    cnt = 0
    for i in range(1, num+1):
        if i < 100:
            cnt += 1
        else:
            han = set()
            for j in range(1, len(str(i))):
                num1 = int(str(i)[j])
                num2 = int(str(i)[j-1])
                han.add(num1 - num2)
        
            if len(han) == 1:
                cnt += 1
    return cnt

print(han(n))


# num = int(input())
# hansu = 0

# for n in range(1, num+1) :
#     if n <= 99 : # 1부터 99까지는 모두 한수
#         hansu += 1 
    
#     else :     
#         nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리 
#         if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
#             hansu+=1

# print(hansu)