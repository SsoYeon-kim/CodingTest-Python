h, m = map(int, input().split())
t = int(input())

over_h = t // 60
over_m = t % 60

hour = h + over_h
min = m + over_m


if min >= 60:
    hour = hour + min//60
    min = min % 60

    if hour >= 24:
        hour = hour % 24

    print(hour,min)
else:
    print(hour,min)