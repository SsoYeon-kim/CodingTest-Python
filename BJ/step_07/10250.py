'''
case = int(input())

for i in range(case):
    floor, room, guest = map(str, input().split())
    assign = ''

    if int(guest) < int(floor):
        assign = guest + '01'
    else:
        assign_floor = int(guest) % int(floor)
        if assign_floor == 0:
            assign_floor = floor
            assign_room = int(guest) // int(floor)
            assign = str(assign_floor) + str(assign_room).zfill(2)
        else:
            assign_room = int(guest) // int(floor) + 1
            assign = str(assign_floor) + str(assign_room).zfill(2)
            
    print(assign)
'''

case = int(input())

for _ in range(case):
    H, W, N = map(int, input().split())

    if not N % H :
        floor = H
        number = N // H
    else:
        floor = N % H
        number = N // H + 1
    
    print(floor*100 + number)