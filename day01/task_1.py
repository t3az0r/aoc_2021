

helloFile = open('input.txt')

arrContent = helloFile.readlines()

a=0
b=0
count=0
for chi in arrContent:
    i = int(chi)
    b = i
    if b > a:
        count += 1
    a = b

print(count -1) #first increasement does not count
