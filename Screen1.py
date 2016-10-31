from __future__ import print_function
from minmax import minmax
from ChessAI import ChessAI
from Rules import Rules
from ChessBoard import ChessBoard

class Screen():

    def __init__(self):
        self.ChessRules=Rules()
        self.ChessBrd1=ChessBoard()
        self.AI2=minmax()
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
            oppColour='B'
        else:
            print ("AI! It's your turn")
            value=self.AI2.alphabeta(board,colour,5,-999999,999999)
            move=value[1]
            oppColour='W'
            self.ChessBrd1.makeMove(board,move)
        if self.ChessRules.isKingInCheck(board,oppColour):
            if oppColour=='W':
                message="White!"
            else:
                message="Black! AI!"
            if self.ChessRules.isCheckMate(board,oppColour)==True:
                print(message+" CheckMate! You lost!")
                self.checkMate=True
            else:
                print(message+" Your king is in check! Save it! ")
                

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
