def solution(x, y, n):
    # dp table 초기화
    dp = [1e9]*(y+1)
    # dp[x] = x가 x로 되는 최소 연산횟수 = 0 초기화
    dp[x] = 0

    for i in range(x, y+1):
        # x에서부터 연산가능한 숫자들만 보기 위함
        if dp[i] == 1e9:
            continue
        if i + n <= y:
            dp[i+n] = min(dp[i+n], dp[i]+1)
        if i * 2 <= y:
            dp[i*2] = min(dp[i*2], dp[i]+1)
        if i * 3 <= y:
            dp[i*3] = min(dp[i*3], dp[i]+1)
    
    if dp[y] == 1e9:
        return -1
    return dp[y]


print(solution(10,40,5))
# 2

