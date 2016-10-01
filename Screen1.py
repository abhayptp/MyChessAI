from __future__ import print_function
from ChessAI import ChessAI
from Rules import Rules
from ChessBoard import ChessBoard

class Screen():

    def __init__(self):
        self.ChessRules=Rules()
        self.ChessBrd1=ChessBoard()
        self.checkMate=False
        self.AI=ChessAI()

    def draw(self,board):
        ch='A'
        print("  ",end="")
        for i in range(1,9):
            print("%2d "%i,end="")
        print()
        for i in range(8):
            print("%s "%ch,end="")
            for j in range(0,8):
                if board[i][j]!='0':
                    print("%s "%board[i][j],end="")
                else:
                    print("__ ",end="")
            ch=chr(ord(ch)+1)
            print()
        print("\n")

    def play(self,board):
        print ("First turn is for White!")
        colour='W'
        self.draw(board)
        while not self.checkMate:
            self.getInput(board,colour)
            self.draw(board)
            if colour=='B':
                colour='W'
            else:
                colour='B'


    def getInput(self,board,colour):
        if colour=='W':
            print ("White! It's your turn")
            fromSquare=self.getInputFromSquare(board,colour)
            toSquare=self.getInputToSquare(board,colour,fromSquare)
            self.ChessBrd1.makeMove(board,(fromSquare,toSquare))
        else:
            print ("AI! It's your turn")
            move=self.AI.getMove(board,colour)
            oppColour='W'
            #Checking for the check
            if self.ChessRules.isKingInCheck(board,oppColour,move[0],move[1]):
                oppColour=='W'
                message="White"
                self.checkMate=True
                move1=()
                for i in range(8):
                    for j in range(8):
                        if oppColour in board[i][j]:
                            valid=self.ChessRules.getValidMoves(board,colour,(i,j))
                            for move1 in valid:
                                if not self.ChessRules.isKingInCheck(board,oppColour,(i,j),move1):
                                    self.checkMate=False
                                    #print(move1)
                                    break
                if self.checkMate==True:
                    print(message+" CheckMate! You lost!")
                else:
                    print(message+" Your king is in check! Save it!")
            self.ChessBrd1.makeMove(board,move)

    def getInputFromSquare(self,board,colour):
        row=0
        column=0
        flag=False
        st=raw_input("Enter from square! ")
        if st!="" and len(st)!=1:
            print (st)
            row=ord(st[0])-65
            column=ord(st[1])-49
        if st=="":
            print("Invalid Input")
            flag=True
        elif len(st)!=2:
            print("Invalid Input")
            flag=True
        elif row<0 or row>7 or column<0 or column>7:
            print("Invalid Input")
            flag=True
        elif board[row][column]=='0':
            print(" Nothing There!")
        elif colour not in board[row][column]:
            print (" That is not your piece!")
        elif not self.ChessRules.getValidMoves(board,(row,column)):
            print (" No Valid moves for that piece!")
        while st=="" or flag or colour not in board[row][column] or len(self.ChessRules.getValidMoves(board,(row,column)))==0:
            flag=False
            st=raw_input("Enter from square! ")
            if st!="" and len(st)!=1:
                row=ord(st[0])-65
                column=ord(st[1])-49
                print (st)
                row=ord(st[0])-65
                column=ord(st[1])-49
                if len(st)!=2:
                    print("Invalid Input")
                    flag=True
                elif row<0 or row>7 or column<0 or column>7:
                    print("Invalid Input")
                    flag=True
                elif board[row][column]=='0':
                   print(" Nothing There!")
                elif colour not in board[row][column]:
                   print (" That is not your piece!")
                elif not self.ChessRules.getValidMoves(board,(row,column)):
                   print (" No Valid moves for that piece!")
            else:
                print("Invalid Input")
        return (row,column)

    def getInputToSquare(self,board,colour,fromTuple):
        validMoveTuple=self.ChessRules.getValidMoves(board,fromTuple)
        self.printMoves(validMoveTuple)
        st=raw_input("Enter to square! ")
        flag=False
        if st!="" and len(st)!=1:
            print (st)
            row=ord(st[0])-65
            column=ord(st[1])-49
            toTuple=(row,column)
        if colour=='W':
            oppColour='B'
        else:
            oppColour='W'
        if st=="":
            print("Invalid Input")
            flag=True
        elif len(st)!=2:
            print("Invalid Input")
            flag=True
        elif row<0 or row>7 or column<0 or column>7:
            print("Invalid Input")
            flag=True
        elif toTuple not in validMoveTuple:
            print (" Invalid Move")
        elif self.ChessRules.isKingInCheck(board,colour,fromTuple,toTuple):
            flag=True
            print("Invalid Input, King is in check")
        while flag or toTuple not in validMoveTuple:
            flag=False
            st=raw_input("Enter to square! ")
            if st!="" and len(st)!=1:
                print (st)
                row=ord(st[0])-65
                column=ord(st[1])-49
                toTuple=(row,column)
            if st=="":
                flag=True
                print("Invalid Input")
            if len(st)!=2:
                print("Invalid Input")
                flag=True
            elif row<0 or row>7 or column<0 or column>7:
                print("Invalid Input")
                flag=True
            elif toTuple not in validMoveTuple:
                print (" Invalid Move")
            elif self.ChessRules.isKingInCheck(board,colour,fromTuple,toTuple):
                print("Invalid Input, King is in check")
                flag=True
        if self.ChessRules.isKingInCheck(board,oppColour,fromTuple,toTuple):
            if oppColour=='W':
                message="White!"
            else:
                message="Black!"
            self.checkMate=True
            move=()
            for i in range(8):
                for j in range(8):
                    if oppColour in board[i][j]:
                        valid=self.ChessRules.getValidMoves(board,(i,j))
                        for move in valid:
                            if not self.ChessRules.isKingInCheck(board,oppColour,(i,j),move):
                                self.checkMate=False
                                #print(move)
                                break
            if self.checkMate==True:
                print(message+" CheckMate! You lost!")
            else:
                print(message+" Your king is in check! Save it! ")

        return (row,column)

    def printMoves(self,validMoveTuple):
        print("Valid Moves")
        for move in validMoveTuple:
            row=move[0]
            rowCh=chr(65+row)
            column=move[1]
            columnCh=chr(49+column)
            print("%c%c "%(rowCh,columnCh),end="")
        print()

    def isGameOver(self,board):
        count=0
        for i in range(8):
                for j in range(8):
                        if 'a' in board[i][j]:
                                count=count+1
        if count==2:
                return False
        else:
            print ("GAME OVER")
            return True
