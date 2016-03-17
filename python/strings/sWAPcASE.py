string = ""
for i in raw_input():
    if (i.islower()):
        string += i.upper()
    else:
        string += i.lower()
print string