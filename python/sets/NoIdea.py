def read():
    return map(int,raw_input().split())
nums = read(); array = read(); Aset = set(read()); Bset = set(read())
print len([i for i in array if (i in Aset and i not in Bset)]) - len([i for i in array if (i in Bset and i not in Aset)])