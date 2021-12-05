import re


helloFile = open('input.txt')

arrContent = helloFile.readlines()

x=0
y=0
aim=0
for line in arrContent:
    matchObj = re.match( r'(.*) (.*)', line, re.M|re.I)
    if matchObj:
        #print ("matchObj.group() : ", matchObj.group())
        #print ("matchObj.group(1) : ", matchObj.group(1))
        #print ("matchObj.group(2) : ", matchObj.group(2))
        direction = matchObj.group(1)
        amount = int(matchObj.group(2))

        if direction == "forward":
            x += amount
            y += (aim * amount)

        if direction == "up":
            aim -= amount

        if direction == "down":
            aim += amount

print("x:", x, "; y:", y)
print("x*y=", x*y)
