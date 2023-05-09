from collections import deque

def solution(maps):
    answer = []
    h, w = len(maps), len(maps[0])
    q = deque()
    visited = set()

    for i in range(h):
        for j in range(w):
            if maps[i][j]!='X' and (i,j) not in visited: # maps를 돌면서 X가 아닌 곳에서부터 bfs
                q.append((i,j))
                day = 0

                while q:
                    x, y = q.popleft()
                    if (x,y) in visited:
                        continue
                    visited.add((x,y))
                    day += int(maps[x][y])
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and maps[nx][ny]!='X' and (nx,ny) not in visited:
                            q.append((nx,ny))
                
                answer.append(day)
    
    return sorted(answer) if answer else [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
# [1,1,27]
