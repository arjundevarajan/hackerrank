raw_input()
n = raw_input().split()
for i in range(len(n)):
    n[i] = int(n[i])
T = tuple(n)
print(hash(T))