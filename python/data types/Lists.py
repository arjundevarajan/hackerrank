L = []
num = int(raw_input())
for i in range(num):
    command = raw_input().split()
    comm = command[0]
    if (comm=="append"):
        L.append(int(command[1]))
    if (comm=="insert"):
        L.insert(int(command[1]),int(command[2]))
    if (comm=="remove"):
        L.remove(int(command[1]))
    if (comm=="pop"):
        L.pop()
    if (comm=="index"):
        L.index(int(command[1]))
    if (comm=="count"):
        L.count(int(command[1]))
    if (comm=="sort"):
        L.sort()
    if (comm=="reverse"):
        L.reverse()
    if (comm=="print"):
        print L