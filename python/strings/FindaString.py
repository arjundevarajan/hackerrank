word, fragment = raw_input(), raw_input()
numTimes = 0
for i in range(len(word)):
    if (i+len(fragment)<=len(word)):
        if word[i:i+len(fragment)] == fragment:
            numTimes += 1
print numTimes