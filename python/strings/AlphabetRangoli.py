n = int(raw_input())
letters = 'abcdefghijklmnopqrstuvwxyz'

def printing(finalList,addition):
    finalList.reverse()
    finalList.extend(addition)
    line = '-'.join(finalList)
    if (len(line)==(n*4-3)):
        print line
    else:
        print line.center(n*4-3,'-')
        
for i in range(n):
    printing(list(letters[n-i:n]),list(letters[n-i-1:n]))
    
for i in range(n-1):
    printing(list(letters[i+2:n]),list(letters[i+1:n]))