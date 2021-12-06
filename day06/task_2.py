import re


helloFile = open('test_input.txt')
#helloFile = open('input.txt')

MAXDAYS = 256

arrContent = helloFile.readlines()

def processOneDay(fish = []):
    countSpawn = 0
    for i in range(len(fish)):
        val = fish[i]
        if val == 0:
            countSpawn += 1
            fish[i] = 6
        else:
            fish[i] -= 1
    for j in range(countSpawn):
        fish.append(8)

fish = []

for line in arrContent:
    seq = line.rstrip()
    for n in seq.split(','):
        print(n)
        fish.append(int(n))

    for d in range(18):
        processOneDay(fish)
        print("day ",(d+1), "; len: ",len(fish))
        #print("After ",str(d+1)," days: ", fish)
    print("len:", len(fish))

    for d in range(MAXDAYS-18):

        processOneDay(fish)
        print("day ",(d+18+1), "; len: ",len(fish))
        #print("After ",str(d+1)," days: ", fish)
    print("len:", len(fish))

    
