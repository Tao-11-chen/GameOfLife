global ROWS
global COLS
ROWS = 20
COLS = 60
def main():
    instruction()
    alist = initialize()                               
    printState(alist)
    blist = neighbor_count(alist)
    future = updateState(alist,blist)
    printState(future)
    a = user_say_yes()
    while a == 'y' or a == 'Y':
        blist = neighbor_count(future)
        future = updateState(alist,blist)
        printState(future)
        a = user_say_yes()

def instruction():
    print("Welcome to Conway's game of life")
    print("This game uses a grid of size 20 by 60 in which")
    print("each cell can either be occupied by an organism or not")
    print("The occupied cells change from generation to generation")
    print("according to the number of neighboring cells which are alive")


def initialize():
    alist = [[0 for i in range(COLS)]for i in range(ROWS)]
    while True:
        row,col = eval(input("请输入行和列，中间用逗号隔开，输入-1，-1则停止："))
        if row<=-1 or col<=-1:
            break
        elif row>20 or col>60:
            print('输入错误，请重新输入')
        else:
            alist[row][col] = 1
    return alist
    
def neighbor_count(alist):
    blist = [[0 for i in range(COLS)]for i in range(ROWS)]
    for l in range(1,ROWS-1):
        for m in range(1,COLS-1):    
            livingneighbours = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    livingneighbours += alist[l + i][m + j]    
            livingneighbours = livingneighbours - alist[l][m]
            blist[l][m] = livingneighbours
    return blist

def updateState(alist,blist):
    future = [[0 for i in range(COLS)]for i in range(ROWS)]
    for l in range(1, ROWS-1):
        for m in range(1,COLS-1):            
            if ((alist[l][m] == 1) and (blist[l][m] < 2)):
                future[l][m] = 0			
            elif ((alist[l][m] == 1) and (blist[l][m] > 3)):	
                future[l][m] == 0
            elif ((alist[l][m] == 0) and (blist[l][m] == 3)):
                future[l][m] = 1
            else:
                future[l][m] = alist[l][m]
    return future

def user_say_yes():
    a = input("输入‘y’或者‘n’来继续或者停止：")
    return a

def printState(alist):
    for each in alist:
        for single in each:
            if single == 1:
                print( "*" , end =" ") 
            else:
                print(" ", end =" ")
        print(end='\n')
    print()


if __name__ == "__main__":
    main()
