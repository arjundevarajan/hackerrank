A = set(map(int,raw_input().split()))
word = 'True'
for i in range(input()):
    B = set(map(int,raw_input().split()))
    if not (A.issuperset(B) and B.issubset(A) and (A is not B)):
        word = 'False'
print word