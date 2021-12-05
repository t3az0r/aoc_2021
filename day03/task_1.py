import re


helloFile = open('input.txt')

arrContent = helloFile.readlines()

bitcount0 = [0,0,0,0,0,0,0,0,0,0,0,0]
bitcount1 = [0,0,0,0,0,0,0,0,0,0,0,0]

gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]


for line in arrContent:
    matchObj = re.match( r'([0-1])([0-1])([0-1])([0-1])([0-1])([0-1])([0-1])([0-1])([0-1])([0-1])([0-1])([0-1])', line, re.M|re.I)
    if matchObj:
        for j in range(12):
            v = int(matchObj.group(j+1))
            if v == 0:
                bitcount0[j] += 1
            if v == 1:
                bitcount1[j] += 1
print("1:",bitcount0)
print("0:",bitcount1)

for j in range(12):
    if bitcount1[j] > bitcount0[j]:
        gamma[j] = 1
        epsilon[j] = 0
    elif bitcount0[j] > bitcount1[j]:
        gamma[j] = 0
        epsilon[j] = 1
    else:
        print("ERROR equal bitcounts")

print("gamma:  ",gamma)
print("epsilon:",epsilon)

i_gamma = 0
i_epsilon = 0
for j in range(12):
    i_gamma += gamma[11-j] * (2**j)
    i_epsilon += epsilon[11-j] * (2**j)

print("i_gamma:  ",i_gamma)
print("i_epsilon:",i_epsilon)

print("power consumption (gamm*epsilon)=", i_gamma*i_epsilon)
