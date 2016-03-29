n = raw_input(); s = set(map(int, raw_input().split())); n = input()
for i in range(n):
    command = raw_input().split()
    if len(s)>0 and command[0]=="pop":
        s.pop()
    if command[0]=="discard" and int(command[1]) in s:
        s.discard(int(command[1]))
    if command[0]=="remove" and int(command[1]) in s:
        s.remove(int(command[1]))
print sum(s)