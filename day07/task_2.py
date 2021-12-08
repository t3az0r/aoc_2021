

#helloFile = open('test_input.txt')
helloFile = open('input.txt')

arrContent = helloFile.readlines()

def diffFun(a, b):
    if a==b: return 0
    n=abs(a-b)
    return n*(n+1)/2

"""
#tests
print(diffFun(2,2))
print(diffFun(2,3))
print(diffFun(3,2))
print(diffFun(2,4))
print(diffFun(4,2))
print(diffFun(2,5))
print(diffFun(5,2))
print(diffFun(2,6))
print(diffFun(6,2))
print(diffFun(12,16))
print(diffFun(16,12))
"""

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
        sum += diffFun(arrValue[j], i)
    fuelSums.append(sum)

print(fuelSums)
print(min(fuelSums))
print(fuelSums.index(min(fuelSums)))
