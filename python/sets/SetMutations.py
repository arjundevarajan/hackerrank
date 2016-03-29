n = input(); s = set(map(int,raw_input().split())); n = input()
for i in range(n):
    command = raw_input().split()
    if command[0]=='intersection_update':
        s &= set(map(int,raw_input().split()))
    if command[0]=='update':
        s |= set(map(int,raw_input().split()))
    if command[0]=='symmetric_difference_update':
        s ^= set(map(int,raw_input().split()))
    if command[0]=='difference_update':
        s -= set(map(int,raw_input().split()))
print sum(s)