raw_input()
S1 = set(map(int,raw_input().split()))
raw_input()
S2 = set(map(int,raw_input().split()))
L = []
L.extend(S1.difference(S2))
L.extend(S2.difference(S1))
L.sort()
for i in L:
    print i