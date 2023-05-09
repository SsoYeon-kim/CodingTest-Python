def solution(sequence, k):
    end = 0
    total = 0
    res = list()

    for i in range(len(sequence)):
        while total < k and end < len(sequence):
            total += sequence[end]
            end += 1
        
        if total == k:
            # 시작 인덱스, 끝 인덱스, 길이
            res.append([i, end-1, end-1-i])
        
        total -= sequence[i]
    
    # 길이가 짧은 순으로 오름차순 정렬
    res = sorted(res, key=lambda x:x[2])

    return res[0][:2]

print(solution([1, 2, 3, 4, 5], 7))
# [2,3]
