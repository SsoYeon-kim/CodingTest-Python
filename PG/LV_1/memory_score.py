def solution(name, yearning, photo):
    answer = []
    # O(n) : n=name, yearning 길이
    dic = dict(zip(name, yearning))
    
    # O(m)
    for ph in photo:
        total = 0
        # O(k)
        for p in ph:
            val = dic.get(p, 0)
            total += val
        answer.append(total)
    
    return answer 

# 시간복잡도 : O(n + m*k)
# n,m 최대 : 100, k 최대 : 7 => 7000