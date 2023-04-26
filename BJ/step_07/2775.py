case = int(input())

for _ in range(case):
    k = int(input())
    n = int(input())

    before = [i for i in range(1, n+1)]
    for i in range(0, k):
        room = list()
        room.append(1)
        
        for j in range(1, n):
            people = before[j] + room[j-1]
            room.append(people)
        before = room
    
    print(room[n-1])
        