import re


# helloFile = open('test_input.txt')
helloFile = open('input.txt')

arrContent = helloFile.readlines()

opener = ['(', '[', '{', '<']
closer = [')', ']', '}', '>']

corruptors = []
allFinishPatterns = []
for line in arrContent:
    line = line.rstrip();
    corrupted = False
    stack = []
    # read line character-wise
    for j in range(len(line)):
        ch = line[j]
        if ch in opener:
            stack.append(ch)
        if ch in closer:
            try:
                head = stack.pop()
                if ch == ')' and head == '(':
                    pass
                elif ch == ']' and head == '[':
                    pass
                elif ch == '}' and head == '{':
                    pass
                elif ch == '>' and head == '<':
                    pass
                else:
                    #print("corruption detected:", line, "; j:", j, "; ch:", ch, "; head:", head)
                    corruptors.append(ch)
                    corrupted = True
            except IndexError as err:
                print("IndexError error: {0}|{1}".format(j, ch))
    if len(stack) > 0 and not corrupted:
        #print("incomplete line:", line)
        #print("stack: ", stack, "-", end='')
        finishPattern = []
        while len(stack) > 0 :
            ch = stack.pop()
            if ch == '(':
                #print(')', end='')
                finishPattern.append(')')
            elif ch == '[':
                #print(']', end='')
                finishPattern.append(']')
            elif ch == '{':
                #print('}', end='')
                finishPattern.append('}')
            elif ch == '<':
                #print('>', end='')
                finishPattern.append('>')
        allFinishPatterns.append(finishPattern)
        #print('.')    

allScores = []
for pattern in allFinishPatterns:
    score = 0
    #print(pattern)
    for i in range(len(pattern)):
        score *= 5
        ch = pattern[i]
        if ch == ')':
            score += 1
        elif ch == ']':
            score += 2
        elif ch == '}':
            score += 3
        elif ch == '>':
            score += 4
        #print("pattern:", pattern, "score:", score)

    #print("score:", score)
    allScores.append(score)

allScores.sort();

print("allScores:", allScores)
n = len(allScores)
print("len-allScores:", n)
m = n//2 +1
print("mid-allScores:", m)
print(allScores[m-1])


