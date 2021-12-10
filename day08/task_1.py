import re


helloFile = open('input.txt')

arrContent = helloFile.readlines()

sum1478 = 0
for line in arrContent:
    matchObj = re.match( r'^.* \| ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+)$', line, re.M|re.I)
    if matchObj:
        w1 = matchObj.group(1)
        w2 = matchObj.group(2)
        w3 = matchObj.group(3)
        w4 = matchObj.group(4)
        if len(w1) in (2,3,4,7): sum1478 += 1
        if len(w2) in (2,3,4,7): sum1478 += 1
        if len(w3) in (2,3,4,7): sum1478 += 1
        if len(w4) in (2,3,4,7): sum1478 += 1

print(sum1478)