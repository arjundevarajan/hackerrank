from __future__ import division
n = int(raw_input())
names = {}
for i in range(0,n):
    person = raw_input()
    per = person.split()
    sum = 0 
    for j in range(1,len(per)):
        sum += float(per[j])
    names[per[0]] = sum/(len(per)-1)
finalName = raw_input()
print "%.2f" % names[finalName]