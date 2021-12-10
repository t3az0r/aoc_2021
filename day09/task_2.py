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


def stepN(grid, x, y):
    if y==0: return None
    else: return grid[x][y-1]

def stepE(grid, x, y):
    if x==rowcnt-1: return None
    else: return grid[x+1][y]

def stepS(grid, x, y):
    if y==colmax-1: return None
    else: return grid[x][y+1]

def stepW(grid, x, y):
    if x==0: return None
    else: return grid[x-1][y]

lowPoints = []

risk = 0
for i in range(rowcnt):
    for j in range(colmax):
        # print(".", i, ",", j, "=", grid[i][j])
        try:
            low, val = isLowPoint(grid, i, j, rowcnt, colmax)
            if low:
                # print(i,",",j,":",val)
                lowPoints.append((i,j))
        except IndexError as err:
            print("IndexError error: {0}|{1}".format(i ,j))

print(lowPoints)

def fillBasin(basin, marked):
    newComer = set()
    """
    print("-----------")
    print("newComer",newComer)
    print("basin",basin)
    print("marked",marked)
    print("-----------")
    """
    for lp in basin:
        if lp in marked:
            # print("gotit:",lp)
            pass
        else:
            marked.add(lp)
            x=lp[0]
            y=lp[1]
            N = stepN(grid, x, y)
            if None!=N and N<9: newComer.add((x, y-1))
            E = stepE(grid, x, y)
            if None!=E and E<9: newComer.add((x+1, y))
            S = stepS(grid, x, y)
            if None!=S and S<9: newComer.add((x, y+1))
            W = stepW(grid, x, y)
            if None!=W and W<9: newComer.add((x-1, y))
    """
    print("-----------")
    print("newComer",newComer)
    print("basin",basin)
    print("marked",marked)
    print("-----------")
    """
    basin = basin.union(newComer)
    if len(basin) != len(marked):
        basin = fillBasin(basin, marked)
    else:
        print("return:", basin)
        return basin
    return basin

allLengths = []

for lp in lowPoints:
    basin = set()
    marked = set()
    basin.add(lp)
    basin = fillBasin(basin, marked)
    #print(basin)
    #print(len(basin))
    allLengths.append(len(basin))

print(allLengths)

allLengths.sort()

print(allLengths[-3:])
p=1
for f in allLengths[-3:]:
    p *= f

print(p)


