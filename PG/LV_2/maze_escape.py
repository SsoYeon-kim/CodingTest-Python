from collections import deque

def solution(maps):
    q = deque()
    visited = set()
    after_l = False
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                q.append((i,j,0))
                visited.add((i,j))
    while q:
        x, y, cnt = q.popleft()
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx, y+dy
            if (nx,ny) not in visited and 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny]!='X':
                # S->L (L을 지나친 후) L->E
                if after_l==False and maps[nx][ny]=='L':
                    after_l = True
                    visited.clear()
                    q.clear()
                    q.append((nx,ny,cnt+1))
                    visited.add((nx,ny))
                    break
                q.append((nx,ny,cnt+1))
                visited.add((nx,ny))
            if after_l==True and 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny]=='E':
                return cnt+1
            continue
    return -1

print(solution(["SOLO","OOXO","OEOO"]))
