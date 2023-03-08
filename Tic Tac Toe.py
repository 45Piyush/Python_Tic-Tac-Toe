#Program To Create Tic Tac Toe Game
def sum(a, b, c):
    return a+b+c

def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"      {zero}  |  {one}  |  {two}  ")
    print(f"    ----------------")
    print(f"      {three}  |  {four}  |  {five}  ")
    print(f"    ----------------")
    print(f"      {six}  |  {seven}  |  {eight}  ")

def checkWin(xState, zState):
    wins = [ [0,1,2], [0,3,6], [0,4,8], [1,4,7], [2,5,8], [3,4,5], [6,7,8], [2,4,6]]
    for  win in wins:
        if( sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print(" X Wins The Game")            
        if( sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print(" Y Wins The Game")
            return 0
    return -1
        
if __name__ == "__main__" :
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("\n \t \t WELCOME TO TIC-TAC-TOE GAME")
    printBoard(xState, zState)
    turn = 1
    while(True):
        if(turn == 1):
            print("\n \t  X Turn ")
            value = int(input("Plz Enter The Value : "))
            xState[value] = 1
            printBoard(xState, zState)
        else:
            print("\n \t  Y Turn ")
            value = int(input("Plz Enter The Value : "))
            zState[value] = 1
            printBoard(xState, zState)

        cWin = checkWin(xState, zState)
        if( cWin !=  -1):
            print("Match Over ")
            break

        turn = 1 - turn
        
            
    
    
