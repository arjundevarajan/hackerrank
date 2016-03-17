word = list(raw_input())
line = raw_input().split()
word[int(line[0])] = line[1]
print ''.join(word)