raw_input()
L = map(int,raw_input().split())
L.sort()
max = L.pop()
while(L[len(L)-1]==max):
    L.pop()
print L.pop()