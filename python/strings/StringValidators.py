word = raw_input()
for i in range(len(word)):
    if word[i].isalnum():
        print word[i].isalnum()
        break
    if ((len(word)-1)==i):
        print word[i].isalnum()
for i in range(len(word)):
    if word[i].isalpha():
        print word[i].isalpha()
        break
    if ((len(word)-1)==i):
        print word[i].isalpha()
for i in range(len(word)):
    if word[i].isdigit():
        print word[i].isdigit()
        break
    if ((len(word)-1)==i):
        print word[i].isdigit()
for i in range(len(word)):
    if word[i].islower():
        print word[i].islower()
        break
    if ((len(word)-1)==i):
        print word[i].islower()
for i in range(len(word)):
    if word[i].isupper():
        print word[i].isupper()
        break
    if ((len(word)-1)==i):
        print word[i].isupper()