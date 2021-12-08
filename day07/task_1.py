

#helloFile = open('test_input.txt')
helloFile = open('input.txt')

arrContent = helloFile.readlines()

# only one line
line = arrContent[0]
arrValue = []
for chi in line.split(','):
    i = int(chi)
    arrValue.append(i)

print(len(arrValue))
# search max,min
MAX = max(arrValue)
MIN = min(arrValue)
print(MAX)
print(MIN)

fuelSums = []
for i in range(MAX+1):
    sum = 0
    for j in range(len(arrValue)):
        sum += abs(arrValue[j] - i)
    fuelSums.append(sum)

print(fuelSums)
print(min(fuelSums))
print(fuelSums.index(min(fuelSums)))
