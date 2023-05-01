def solution(park, routes):
    h, w = len(park), len(park[0])

    start_x, start_y = 0, 0
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                start_x , start_y = j, i
                break
    
    for r in routes:
        xx = start_x
        yy = start_y
        for step in range(int(r[2:])):
            if r[0] == 'E' and xx != w-1 and park[yy][xx+1] != 'X':
                xx += 1
                if step == int(r[2:])-1:
                    start_x = xx
            elif r[0] == 'W' and xx != 0 and park[yy][xx-1] != 'X':
                xx -= 1
                if step == int(r[2:])-1:
                    start_x = xx
            elif r[0] == 'N' and yy != 0 and park[yy-1][xx] != 'X':
                yy -= 1
                if step == int(r[2:])-1:
                    start_y = yy
            elif r[0] == 'S' and yy != h-1 and park[yy+1][xx] != 'X':
                yy += 1
                if step == int(r[2:])-1:
                    start_y = yy
    
    return [start_y, start_x]