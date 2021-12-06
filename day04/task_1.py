

class BingoBoard:
    """ 5x5 grid """

    def __init__(self, name):
        self.name = name
        self.numberBoard = [[1,1,2,1,1], 
                            [1,0,3,0,0], 
                            [1,0,4,0,0], 
                            [1,0,5,0,0], 
                            [1,0,6,0,0]]
        self.statusBoard = [[False,False,False,False,False], 
                            [False,False,False,False,False], 
                            [False,False,False,False,False], 
                            [False,False,False,False,False], 
                            [False,False,False,False,False]]

    def has(self, number):
        for i in range(5):
            row  = self.numberBoard[i]
            for j in range(5):
                if row[j] == number:
                    print("found ", number, " at (",i,",",j,")")
                    return (i, j)

    def get(self, x, y):
        return self.numberBoard[x][y]

    def set(self, x, y, val):
        self.numberBoard[x][y] = val

    def setActive(self, x, y, val):
        self.statusBoard[x][y] = val

    def isBingo(self):
        sb = self.statusBoard
        # rows
        if   sb[0][0] and sb[0][1] and sb[0][2] and sb[0][3] and sb[0][4]: return True
        elif sb[1][0] and sb[1][1] and sb[1][2] and sb[1][3] and sb[1][4]: return True
        elif sb[2][0] and sb[2][1] and sb[2][2] and sb[2][3] and sb[2][4]: return True
        elif sb[3][0] and sb[3][1] and sb[3][2] and sb[3][3] and sb[3][4]: return True
        elif sb[4][0] and sb[4][1] and sb[4][2] and sb[4][3] and sb[4][4]: return True

        #cols
        if   sb[0][0] and sb[1][0] and sb[2][0] and sb[3][0] and sb[4][0]: return True
        elif sb[0][1] and sb[1][1] and sb[2][1] and sb[3][1] and sb[4][1]: return True
        elif sb[0][2] and sb[1][2] and sb[2][2] and sb[3][2] and sb[4][2]: return True
        elif sb[0][3] and sb[1][3] and sb[2][3] and sb[3][3] and sb[4][3]: return True
        elif sb[0][4] and sb[1][4] and sb[2][4] and sb[3][4] and sb[4][4]: return True

        #diags
        # if   sb[0][0] and sb[1][1] and sb[2][2] and sb[3][3] and sb[4][4]: return True
        # elif sb[0][4] and sb[1][3] and sb[2][2] and sb[3][1] and sb[4][0]: return True

        return False

    def draw(self, number):
        (cx, cy) = self.has(number)
        print(cx, cy)
        if cx or cy:
            self.setActive(cx, cy, True)

    def print(self):
        for i in range(5):
            row  = self.numberBoard[i]
            srow = self.statusBoard[i]
            for j in range(5):
                if srow[j]: print('*', end='')
                else: print(' ', end='')
                print(row[j], end='')
                if srow[j]: print('*', end='')
                else: print(' ', end='')
                print(' ', end='')
            print('')
        print('----------------------------')

def __main__():
    bb1 = BingoBoard('bb1')
    print(bb1.name)
    bb1.print()
    bb1.setActive(4,2,True)
    bb1.print()

    bb1.set(4,2,45)
    bb1.set(4,3,44)
    bb1.print()

    print(bb1.get(4,2))

    bb1.setActive(4,2,False)
    bb1.print()

    bb1.draw(45)
    bb1.print()
    print(bb1.isBingo())

    bb1.draw(2)
    bb1.print()
    print(bb1.isBingo())

    bb1.draw(3)
    bb1.print()
    print(bb1.isBingo())

    bb1.draw(4)
    bb1.print()
    print(bb1.isBingo())

    bb1.draw(5)
    bb1.print()
    print(bb1.isBingo())




__main__()


