import re


# helloFile = open('test_input.txt')
helloFile = open('input.txt')

arrContent = helloFile.readlines()

grid=[]
rowcnt=0
colmax=0
for line in arrContent:
    line = line.rstrip();
    row=[]
    for j in range(len(line)):
        i = int(line[j])
        row.append(i)
    grid.append(row)
    rowcnt += 1
    if len(row) > colmax: colmax = len(row)

print(grid)
print(rowcnt)

print(colmax)

print(grid[1][2])

def isLowPoint(grid, x, y, rowmax, colmax):
    val = grid[x][y] 
    if x==0 and y==0:
        if grid[x+1][y] > val and grid[x][y+1] > val: return (True, val)
    elif x==0 and y==colmax-1:
        if grid[x+1][y] > val and grid[x][y-1] > val: return (True, val)
    elif x==rowmax-1 and y==0:
        if grid[x-1][y] > val and grid[x][y+1] > val: return (True, val)
    elif x==rowmax-1 and y==colmax-1:
        if grid[x-1][y] > val and grid[x][y-1] > val: return (True, val)
    elif x==0:
        if grid[x+1][y] > val and grid[x][y-1] > val and grid[x][y+1] > val: return (True, val)
    elif x==rowmax-1:
        if grid[x-1][y] > val and grid[x][y-1] > val and grid[x][y+1] > val: return (True, val)
    elif y==0:
        if grid[x-1][y] > val and grid[x+1][y] > val and grid[x][y+1] > val: return (True, val)
    elif y==colmax-1:
        if grid[x-1][y] > val and grid[x+1][y] > val and grid[x][y-1] > val: return (True, val)
    else:
        if grid[x-1][y] > val and grid[x+1][y] > val and grid[x][y-1] > val and grid[x][y+1] > val : return (True, val)

    return (False, None)


risk = 0
for i in range(rowcnt):
    for j in range(colmax):
        # print(".", i, ",", j, "=", grid[i][j])
        try:
            low, val = isLowPoint(grid, i, j, rowcnt, colmax)
            if low:
                print(i,",",j,":",val)
                risk += val+1
        except IndexError as err:
            print("IndexError error: {0}|{1}".format(i ,j))

print(risk)
