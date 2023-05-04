from collections import deque
def solution(board):
    q = deque()
    visited = set()
  
    # 큐에 (시작지점, 시작-현재까지의 거리) 추가
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                q.append((i,j,0))

    while q:
        x, y, cnt = q.popleft()
        if (x, y) in visited:
            continue
        if board[x][y] == 'G':
            return cnt
        visited.add((x,y))
        for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
            # 현재 위치 변수 필요 !
            now_x, now_y = x, y
            while True:
                next_x, next_y = now_x+dx, now_y+dy
                if 0<=next_x<len(board) and 0<=next_y<len(board[0]) and board[next_x][next_y] != 'D':
                    # 이동한 현재위치 초기화 !
                    now_x, now_y = next_x, next_y
                    continue
                # (멈춘 위치, cnt) 큐에 추가
                q.append((now_x, now_y, cnt+1))
                break
    return -1
