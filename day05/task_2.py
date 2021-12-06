import re


# helloFile = open('test_input.txt')
helloFile = open('input.txt')

arrContent = helloFile.readlines()
def dumpBoard(board, xMax, yMax):
    for x in range(xMax):
        column = board[x]
        for y in range(yMax):
            val = column[y]
            if val == 0:
                ch = '.'
            else:
                ch = str(val)
            print(ch, end='')
        print('|')

def isDiagonal(x1, x2, y1, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return (dx==dy)
    

def countBoardMoreThan(board, xMax, yMax, limit):
    total = 0
    for x in range(xMax +1):
        column = board[x]
        for y in range(yMax +1):
            val = column[y]
            if val > limit:
                total += 1
    return total

# init board
xMax=0
yMax=0
# detect max
for line in arrContent:
    matchObj = re.match( r'(\d+),(\d+) -> (\d+),(\d+)', line, re.M|re.I)
    if matchObj:
        x1 = int(matchObj.group(1))
        y1 = int(matchObj.group(2))           
        x2 = int(matchObj.group(3))
        y2 = int(matchObj.group(4))

        if x1 > xMax: xMax = x1;           
        if x2 > xMax: xMax = x2;           
        if y1 > xMax: yMax = y1;           
        if y2 > xMax: yMax = y2;           

board = []
for i in range(1000): #xMax+1):
    column = []
    for j in range(1000): #yMax+1):
        column.append(0)
    board.append(column)
print("xMax:", xMax, "; yMax:", yMax)
print("--------------------------------------------")
#print(board)
#dumpBoard(board, xMax+1, yMax+1)
print("--------------------------------------------")
# -------- init done

# now fill board
for line in arrContent:
    matchObj = re.match( r'(\d+),(\d+) -> (\d+),(\d+)', line, re.M|re.I)
    if matchObj:
        x1 = int(matchObj.group(1))
        y1 = int(matchObj.group(2))           
        x2 = int(matchObj.group(3))
        y2 = int(matchObj.group(4))
    if x1 == x2:   # make vertical line
        if y1 == y2: # simply one 'dot'
            board[y1][x1] += 1
        elif y2 > y1:
            for k in range(y2-y1 +1):
                board[y1+k][x1] += 1
        else:
            for k in range(y1-y2 +1):
                board[y2+k][x2] += 1
    elif y1 == y2: # make horizontal line
        if x1 == x2: # simply one 'dot'
            board[x1][y1] += 1
        elif x2 > x1:
            for k in range(x2-x1 +1):
                board[y1][x1+k] += 1
        else:
            for k in range(x1-x2 +1):
                board[y2][x2+k] += 1
    elif isDiagonal(x1, x2, y1, y2):
        if y2 > y1:
            if x2 > x1:
                for k in range(x2-x1 +1):
                    board[y1+k][x1+k] += 1
            else: # backwards
                for k in range(x1-x2 +1):
                    board[y1+k][x1-k] += 1
        else:
            if x2 > x1: # backwards
                for k in range(x2-x1 +1):
                    board[y1-k][x1+k] += 1
            else:
                for k in range(x1-x2 +1):
                    board[y2+k][x2+k] += 1
    else:
        print("WARN: no straight line: ", line)

print("--------------------------------------------")
#print(board)
#dumpBoard(board, xMax+1, yMax+1)
print("--------------------------------------------")

# now count
print("more than 1:", countBoardMoreThan(board, xMax, yMax, 1))
