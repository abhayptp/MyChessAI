from __future__ import print_function
class ChessBoard:
    def __init__(self):
        self.board=[['Wr','Wh','Wb','Wa','Wq','Wb','Wh','Wr'],
                    ['Wp','Wp','Wp','Wp','Wp','Wp','Wp','Wp'],
                    ['0','0','0','0','0','0','0','0'],
                    ['0','0','0','0','0','0','0','0'],
                    ['0','0','0','0','0','0','0','0'],
                    ['0','0','0','0','0','0','0','0'],
                    ['Bp','Bp','Bp','Bp','Bp','Bp','Bp','Bp'],
                    ['Br','Bh','Bb','Ba','Bq','Bb','Bh','Br']]
        
    def getBoard(self):
        return self.board

    def getForce(self,colour,board):
        return [(i,j) for i in range(8) for j in range(8) if colour in board[i][j]]
    
    def getName(self,piece):
        s=""
        if 'B' in piece:
            s=s+"Black"
        else:
            s=s+"White"
        if 'r' in piece:
            s=s+" Rook"
        elif 'b' in piece:
            s=s+" Bishop"
        elif 'k' in piece:
            s=s+" Knight"
        elif 'p' in piece:
            s=s+" Pawn"
        elif 'q' in piece:
            s=s+" Queen"
        elif 'a' in piece:               #a for King
            s=s+" King"
        return s
	      
        
    def makeMove(self,board,moveTuple):
        #moveTuple1=covertToMatrixNotation(moveTuple)
        toRowPosition=moveTuple[1][0]
        fromRowPosition=moveTuple[0][0]
        toColumnPosition=moveTuple[1][1]
        fromColumnPosition=moveTuple[0][1]
        pp=""
        if board[fromRowPosition][fromColumnPosition]=='Bp' and toRowPosition==7 :  #For Promotion
            pp=raw_input("Enter the piece you want to promote your pawn to: ")
            while len(pp)!=2 and pp[0]=='B' and (pp[1]=='r' or pp[1]=='h' or pp[1]=='b' or pp[1]=='p' or pp[1]=='a' or pp[1]=='q'):
                print("Invalid Input")
                pp=raw_input("Enter the piece you want to promote your pawn to: ")
            board[toRowPosition][toColumnPosition]=pp
            board[fromRowPosition][fromColumnPosition]='0'
        elif board[fromRowPosition][fromColumnPosition]=='Wp' and toRowPosition==0 :  #For Promotion
            pp=raw_input("Enter the piece you want to promote your pawn to: ")
            while len(pp)!=2 and pp[0]=='W' and (pp[1]=='r' or pp[1]=='h' or pp[1]=='b' or pp[1]=='p' or pp[1]=='a' or pp[1]=='q'):
                print("Invalid Input")
                pp=raw_input("Enter the piece you want to promote your pawn to: ")
            board[toRowPosition][toColumnPosition]=pp
            board[fromRowPosition][fromColumnPosition]='0'
        elif board[toRowPosition][toColumnPosition]!='0':
            print (self.getName(board[toRowPosition][toColumnPosition])+" is killed")
            board[toRowPosition][toColumnPosition]=board[fromRowPosition][fromColumnPosition]
            board[fromRowPosition][fromColumnPosition]='0'
        else:
            board[toRowPosition][toColumnPosition]=board[fromRowPosition][fromColumnPosition]
            board[fromRowPosition][fromColumnPosition]='0'
        
        
'''ob=ChessBoard()
board1=[['Wr','Wh','Wb','Wa','Wq','Wb','Wh','Wr'],
            ['Wp','Wp','Wp','Wp','Wp','Wp','Wp','Wp'],
            ['0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0'],
            ['Bp','Bp','Bp','Bp','Bp','Bp','Bp','Bp'],
            ['Br','Bh','Bb','Ba','Bq','Bb','Bh','Br']]
force=ob.getForce('B',board1)
print (force)'''
