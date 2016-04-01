def read():
    return raw_input().split()
nums = map(int,read()); array = map(int,read()); Aset = set(map(int,read())); Bset = set(map(int,read()))
print len([i for i in array if (i in Aset and i not in Bset)]) - len([i for i in array if (i in Bset and i not in Aset)])