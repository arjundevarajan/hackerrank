k = input(); rooms = map(int,raw_input().split()); roomSet = set(rooms)
print ((sum(roomSet)*k)-sum(rooms))/(k-1)