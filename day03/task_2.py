import re


# helloFile = open('input_test.txt')
helloFile = open('input.txt')

arrContent = helloFile.readlines()

def decFromBinary(valArr):
  arrLen = len(valArr)
  res = 0
  for j in range(arrLen):
    res += int(valArr[arrLen -1 -j]) * (2**j)
  return res

def dominatingBitAtIndex(sArray = [], index = 0):
  count0 = 0
  count1 = 0
  for val in sArray:
    bit = int(val[index])
    if bit == 0:
      count0 += 1
    elif bit == 1:
      count1 += 1
    else:
      print("ERROR: unknown bit found:,", val[index], " in ", val, " at index ", index)
  if count0 > count1:
    return 0
  else:
    return 1
# end of dominatingBitAtIndex

def recessiveBitAtIndex(sArray = [], index = 0):
  count0 = 0
  count1 = 0
  for val in sArray:
    bit = int(val[index])
    if bit == 0:
      count0 += 1
    elif bit == 1:
      count1 += 1
    else:
      print("ERROR: unknown bit found:,", val[index], " in ", val, " at index ", index)
  if count1 < count0:
    return 1
  else:
    return 0
# end of recessiveBitAtIndex

def filterArrayOnValueAtIndex(sArray = [], value = 0, index = 0):
  remainder = []
  for val in sArray:
    bit = int(val[index])
    if bit == value:
      remainder.append(val)
  return remainder
# end of filterArrayOnValue

"""
# tests
print(dominatingBitAtIndex(arrContent, 0))
print(dominatingBitAtIndex(arrContent, 1))

print(recessiveBitAtIndex(arrContent, 0))
print(recessiveBitAtIndex(arrContent, 1))

print(filterArrayOnValueAtIndex(arrContent, 1, 0))
print(filterArrayOnValueAtIndex(arrContent, 0, 0))
"""

# main
dim = len(arrContent[0].rstrip())
print(dim)
# oxygen
workingArr = arrContent
for j in range(dim):
  if len(workingArr) == 1:
    break
  dom = dominatingBitAtIndex(workingArr, j)
  workingArr = filterArrayOnValueAtIndex(workingArr, dom, j)

oxy = decFromBinary(workingArr[0].rstrip())

# co2
workingArr = arrContent
for j in range(dim):
  if len(workingArr) == 1:
    break
  rec = recessiveBitAtIndex(workingArr, j)
  workingArr = filterArrayOnValueAtIndex(workingArr, rec, j)

co2 = decFromBinary(workingArr[0].rstrip())

print("oxy:",oxy,"; co2:",co2)
print("oxy*c02=",oxy*co2)
