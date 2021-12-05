

helloFile = open('input.txt')

arrContent = helloFile.readlines()

threeSums = []
tempSum1 = []
tempSum2 = []
tempSum3 = []
index=1
for chi in arrContent:
    i = int(chi)

    tempSum1.append(i)
    if index > 1 :
        tempSum2.append(i)
    if index > 2 :
        tempSum3.append(i)

    if len(tempSum1) == 3:
        # calc and push and empty
        threeSums.append(sum(tempSum1))
        tempSum1 = []
    if len(tempSum2) == 3:
        # calc and push and empty
        threeSums.append(sum(tempSum2))
        tempSum2 = []
    if len(tempSum3) == 3:
        # calc and push and empty
        threeSums.append(sum(tempSum3))
        tempSum3 = []

    index += 1

# print(len(threeSums))
# print(threeSums)

a=0
b=0
count=0
for i in threeSums:
    b = i
    if b > a:
        count += 1
    a = b

print(count -1) #first increasement does not count

