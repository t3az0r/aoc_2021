import re


# helloFile = open('test_input.txt')
helloFile = open('input.txt')

arrContent = helloFile.readlines()

opener = ['(', '[', '{', '<']
closer = [')', ']', '}', '>']

corruptors = []

for line in arrContent:
    line = line.rstrip();
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
            except IndexError as err:
                print("IndexError error: {0}|{1}".format(j, ch))

print(corruptors)

score = 0
for c in corruptors:
    if c == ')':
        score += 3
    elif c == ']':
        score += 57
    elif c == '}':
        score += 1197
    elif c == '>':
        score += 25137
    else:
        pass

print(score)