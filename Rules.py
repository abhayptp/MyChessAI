#a for king, q for queen, b for bishop,, r for rook, k for knight,  p for pawn
#Black is up in the board
class Rules:
        def __init__(self):
                pass
        
        #For checking if this is my piece
        def isMyPiece(self,board,i,j,colour):
                if colour in board[i][j]:
                        return True
                else:
                        return False
                
        #For checking if this (x,y) position is inside the board or not
        def inside(self,x,y):
                if x>=0 and x<8 and y>=0 and y<8:
                        return True
                return False
        
        #For checking if (i,j) pos is safe or not
        def safe(self,i,j,board,color):
		#For diagonal moves of queen and bishop
                for (d1,d2) in ((1,1),(-1,-1),(-1,1),(1,-1)):
                        x=i
                        y=j
                        while True:
                                x+=d1
                                y+=d2
                                if not self.inside(x,y):
                                        break
                                elif board[x][y]!='0':
                                        if not color in board[x][y] and (board[x][y][1] in ('q','b')):
                                                return False
                                        break
                                
                #For horizontal and vertical moves of queen and rook
                for (d1,d2) in ((0,1),(1,0),(0,-1),(-1,0)):
                        x=i
                        y=j
                        while True:
                                x+=d1
                                y+=d2
                                if not self.inside(x,y):
                                        break
                                elif board[x][y]!='0':
                                        if not color in board[x][y] and (board[x][y][1] in ('q','r')):
                                                return False
                                        break
                                
                #For moves of knight
                for (d1,d2) in ((2,1),(-2,-1),(2,-1),(-2,1),(1,2),(-1,-2),(-1,2),(1,-2)):
                        if self.inside(i+d1,j+d2):	
                                if not color in board[i+d1][j+d2] and 'h' in board[i+d1][j+d2]:
                                        return False
                                
                #If colour is black,then it can be killed by only white, and white can only move up in the board
                if color=='B':
                        c=1
                else:
                        c=-1
                        
                #For moves of pawn
                for (d1,d2) in ((c,1),(c,-1)):
                        if self.inside(i+d1,j+d2):	
                                if not color in board[i+d1][j+d2] and 'p' in board[i+d1][j+d2]:
                                        return False
                                
                #For moves of king
                for (d1,d2) in ((-1,-1),(1,-1),(-1,1),(1,1),(0,1),(1,0),(0,-1),(-1,0)):
                        if self.inside(i+d1,j+d2):	
                                if  not color in board[i+d1][j+d2] and 'a' in board[i+d1][j+d2]:
                                        return False
                return True
        
        #For checking if the king is in check or not
        def isKingInCheck(self,board,colour):
                king=colour+'a'
                for i in range(8):
                        for j in range(8):
                                if board[i][j]==king:
                                        (x,y)=(i,j)
                                        break
                if self.safe(x,y,board,colour)==True:
                        return False
                else:
                        return True
                
        #For checking whether it is check mate or not
        def isCheckMate(self,board,colour):
                moves=[]
                #Taking all legal moves of colour in moves
                for i in range(8):
                        for j in range(8):
                                if colour in board[i][j]:
                                        moves.extend(self.getValidMoves(board,(i,j)))
                #If it is checkmate, then there can be no legal move for colour
                if len(moves)==0:
                        return True
                else:
                        return False

        #Checking if it is valid move or not                                                          
        def isValid(self,board,colour,fromTuple,toTuple):
                validMoves=self.getValidMoves(board,fromTuple)
                if (toTuple in validMoves) and self.isKingInCheck(board,colour,fromTuple,toTuple):
                        return True
                else:
                        return False

        #Checking if the path is clear or not
        def isClear(self,board,fromTuple,ToTuple):
                i1=fromTuple[0]
                j1=fromTuple[1]
                i2=ToTuple[0]
                j2=ToTuple[1]
                #Something
                flag=0
                if i1==i2:
                        if j1>j2:
                                j1=j1-1
                                while j1!=j2:
                                        if board[i1][j1]!='0':
                                                flag=1
                                                break
                                        j1=j1-1
                        else:
                                j1=j1+1
                                while j1!=j2:
                                        if board[i1][j1]!='0':
                                                flag=1
                                                break
                                        j1=j1+1
                elif j1==j2:
                        if i1>i2:
                                i1=i1-1
                                while i1!=i2:
                                        if board[i1][j1]!='0':
                                                flag=1
                                                break
                                        i1=i1-1
                        else:
                                i1=i1+1
                                while i1!=i2:
                                        if board[i1][j1]!='0':
                                                flag=1
                                                break
                                        i1=i1+1
                else:
                        if i1<i2 and j1<j2:
                                i1=i1+1
                                j1=j1+1
                                while i1!=i2:
                                        if board[i1][j1]!='0':
                                                flag=1
                                                break
                                        i1=i1+1
                                        j1=j1+1
                        elif i1<i2 and j1>j2:
                                i1=i1+1
                                j1=j1-1
                                while i1!=i2:
                                        if board[i1][j1]!='0':
                                                flag=1
                                                break
                                        i1=i1+1
                                        j1=j1-1
                        elif i1>i2 and j1<j2:
                                i1=i1-1
                                j1=j1+1
                                while i1!=i2:
                                        if board[i1][j1]!='0':
                                                flag=1
                                                break
                                        i1=i1-1
                                        j1=j1+1
                        elif i1>i2 and j1>j2:
                                i1=i1-1
                                j1=j1-1
                                while i1!=i2:
                                        if board[i1][j1]!='0':
                                                flag=1
                                                break
                                        i1=i1-1
                                        j1=j1-1
                if flag==1:
                        return False
                else:
                        return True

        def getValidMoves(self,board,fromMoveTuple): #No need of colour as it has been checked in the getInput function
                fromRow=fromMoveTuple[0]
                fromColumn=fromMoveTuple[1]
                ch=board[fromRow][fromColumn]
                colour=ch[0]
                validMoveTuple=[]
                SingleMove=()
                
                if 'p' in ch:      #For pawn
                        if 'B' in ch:
                                #As pawn can move two pos ahead in its first move
                                if fromRow==1 and self.isClear(board,fromMoveTuple,(3,fromColumn))==True and board[3][fromColumn]=='0':
                                        validMoveTuple.append((3,fromColumn))
                                #If the pawn is killing any piece
                                if fromColumn!=0 and fromRow!=7 and 'W' in board[fromRow+1][fromColumn-1]:
                                    validMoveTuple.append((fromRow+1,fromColumn-1))
                                if fromColumn!=7 and fromRow!=7 and 'W' in board[fromRow+1][fromColumn+1]:
                                    validMoveTuple.append((fromRow+1,fromColumn+1))
                                if fromRow!=7 and board[fromRow+1][fromColumn]=='0':
                                    validMoveTuple.append((fromRow+1,fromColumn))
                        if 'W' in ch:
                                if fromRow==6 and self.isClear(board,fromMoveTuple,(4,fromColumn))==True and board[4][fromColumn]=='0':
                                        validMoveTuple.append((4,fromColumn))
                                if fromColumn!=0 and fromRow!=0 and 'B' in board[fromRow-1][fromColumn-1]:
                                    validMoveTuple.append((fromRow-1,fromColumn-1))
                                if fromColumn!=7 and fromRow!=0 and 'B' in board[fromRow-1][fromColumn+1]:
                                    validMoveTuple.append((fromRow-1,fromColumn+1))
                                if fromRow!=0 and board[fromRow-1][fromColumn]=='0':
                                    validMoveTuple.append((fromRow-1,fromColumn))
                                    
                if 'r' in ch:   #For Rook
                        for i in range(8):
                                if i==fromRow:
                                    continue
                                elif self.isMyPiece(board,i,fromColumn,colour)==False and self.isClear(board,fromMoveTuple,(i,fromColumn))==True:
                                    validMoveTuple.append((i,fromColumn))
                        for j in range(8):
                                if j==fromColumn:
                                    continue
                                elif self.isMyPiece(board,fromRow,j,colour)==False and self.isClear(board,fromMoveTuple,(fromRow,j))==True:
                                        validMoveTuple.append((fromRow,j))
                                                                
                if 'b' in ch:    #For bishop
                        for r in [+1,-1]:
                                for c in [+1,-1]:
                                        i=fromRow
                                        j=fromColumn
                                        while i>=0 and i<8 and j>=0 and j<8:
                                                if i==fromRow or j==fromColumn:
                                                        i=i+r
                                                        j=j+c
                                                        continue
                                                if self.isMyPiece(board,i,j,colour)==True:
                                                        break;
                                                else:
                                                        if board[i][j]!='0':
                                                                validMoveTuple.append((i,j))
                                                                break
                                                validMoveTuple.append((i,j))
                                                i=i+r
                                                j=j+c
                                                
                if 'a' in ch:    #For king
                        for i in [fromRow+1,fromRow-1,fromRow]:
                                if i>=0 and i<8:
                                        for j in [fromColumn+1,fromColumn-1,fromColumn]:
                                                if j>=0 and j<8:
                                                        if self.isMyPiece(board,i,j,colour)==False:
                                                                validMoveTuple.append((i,j))
                #Combining both rook and bishop moves in queen
                if 'q' in ch:         #For Queen
                        for i in range(8):
                                if i==fromRow:
                                    continue
                                elif self.isMyPiece(board,i,fromColumn,colour)==False and self.isClear(board,fromMoveTuple,(i,fromColumn))==True:
                                    validMoveTuple.append((i,fromColumn))
                        for j in range(8):
                                if j==fromColumn:
                                    continue
                                elif self.isMyPiece(board,fromRow,j,colour)==False and self.isClear(board,fromMoveTuple,(fromRow,j))==True:
                                        validMoveTuple.append((fromRow,j))
                        for r in [+1,-1]:
                                for c in [+1,-1]:
                                        i=fromRow
                                        j=fromColumn
                                        while i>=0 and i<8 and j>=0 and j<8:
                                                if i==fromRow or j==fromColumn:
                                                        i=i+r
                                                        j=j+c
                                                        continue
                                                if self.isMyPiece(board,i,j,colour)==True:
                                                        break;
                                                else:
                                                        if board[i][j]!='0':
                                                                validMoveTuple.append((i,j))
                                                                break
                                                validMoveTuple.append((i,j))
                                                i=i+r
                                                j=j+c


                if 'h' in ch:             #For KNIGHT
                        for i in [fromRow+2,fromRow-2]:
                                if i>=0 and i<8:
                                        for j in [fromColumn+1,fromColumn-1]:
                                                if j>=0 and j<8:
                                                        if self.isMyPiece(board,i,j,colour)==False:
                                                                validMoveTuple.append((i,j))
                        for i in [fromRow-1,fromRow+1]:
                                if i>=0 and i<8:
                                        for j in [fromColumn-2,fromColumn+2]:
                                                if j>=0 and j<8:
                                                        if self.isMyPiece(board,i,j,colour)==False:
                                                                validMoveTuple.append((i,j))
                                                        
                validMoves=[]
                king=colour+'a'
                flag=0
                for i in range(8):
                        for j in range(8):
                                if king in board[i][j]:
                                        flag=1
                                        (x,y)=(i,j)
                                        break
                for move in validMoveTuple:
                        c=board[move[0]][move[1]]
                        board[move[0]][move[1]]=ch
                        board[fromRow][fromColumn]='0'
                        if 'a' in ch:
                                flag=1
                                (x,y)=(move[0],move[1])
                        if flag==0:
                                print board
                        if 'a' not in c and self.safe(x,y,board,colour):
                                validMoves.append(move)
                        board[move[0]][move[1]]=c
                        board[fromRow][fromColumn]=ch
                return validMoves
'''
board=[['Br','Bh','Bb','0','Bq','Bb','Bh','Br'],
       ['Bp','Bp','Bp','0','Bp','Bp','Bp','Bp'],
       ['0','0','Wr','0','0','0','0','0'],
       ['0','0','0','0','Ba','0','0','0'],
       ['0','Wq','0','0','0','0','0','0'],
       ['0','0','0','0','0','0','0','0'],
       ['Wp','Wp','Wp','Wp','Wp','Wp','Wp','Wp'],
       ['Wr','Wh','Wb','Wa','0','Wb','Wh','Wr']]
ob=Rules()
valid=ob.getValidMoves(board,(7,6))
print(valid)
'''
