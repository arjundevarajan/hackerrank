n = int(raw_input())
width = len(bin(n).lstrip("0b"))
for i in range(n):
    print str(int(i+1)).rjust(width), str(int(oct(i+1))).rjust(width), hex(i+1).lstrip("0x").upper().rjust(width), bin(i+1).lstrip("0b").rjust(width)