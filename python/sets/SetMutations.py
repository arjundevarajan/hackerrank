n = input(); s = set(map(int,raw_input().split()))
for i in range(input()):
    exec 's.' + raw_input().split()[0] + '(set(map(int,raw_input().split())))'
print sum(s)