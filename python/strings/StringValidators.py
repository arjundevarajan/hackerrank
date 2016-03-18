word = raw_input()
outputs = ["False","False","False","False","False"]
for i in word:
    if i.isalnum():
        outputs[0] = "True"
    if i.isalpha():
        outputs[1] = "True"
    if i.isdigit():
        outputs[2] = "True"
    if i.islower():
        outputs[3] = "True"
    if i.isupper():
        outputs[4] = "True"
for j in outputs:
    print j