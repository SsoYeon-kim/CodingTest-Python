def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []

    for i, val in enumerate(numbers):
        # 스택의 마지막 값부터 비교
        while stack and numbers[stack[-1]] < val:
            # 큰 값으로 사용되면 pop
            answer[stack.pop()]= val
        # 스택에는 numbers의 인덱스 저장
        stack.append(i)
    
    return answer

print(solution([2,3,3,5]))