def solution(wallpaper):

    h , w = len(wallpaper), len(wallpaper[0])
    x, y = [], []
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
    return [min(x), min(y), max(x)+1, max(y)+1]

print(solution([".#...", "..#..", "...#."]))