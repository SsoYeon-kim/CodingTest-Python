def solution(n, m, section):
    answer = 1
    # 시작 시점
    start = section[0]

    # 범위 (다음 시점 - 시작 시점)
    for s in section[1:]:
        # 범위가 롤러 길이를 충족할 경우 덧칠 +1
        if s-start >= m:
            answer += 1
            # 시작 시점 이동
            start = s

    return answer