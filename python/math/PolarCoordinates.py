import cmath
compNum = raw_input().split('+'); compNum[1] = compNum[1].strip('j'); compNum = map(float,compNum)
print cmath.polar(complex(compNum[0], compNum[1]))[0]
print cmath.polar(complex(compNum[0], compNum[1]))[1]