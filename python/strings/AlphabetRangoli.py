n = int(raw_input())
letters = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n):
    print letters[n-i-1].center((n*4)-3,'-')

for i in range(n-1):
    print letters[i+1].center((n*4)-3,'-')