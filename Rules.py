#a for king, q for queen, b for bishop,, r for rook, k for knight,  p for pawn
#Black is up in the board

class Rules:
        def __init__(self):
                pass
        def isMyPiece(self,board,i,j,colour):
                if colour in board[i][j]:
                        return True
                else:
                        return False
        def inside(self,x,y):
                if x>=0 and x<8 and y>=0 and y<8:
                        return True
                return False
        def safe(self,i,j,board,color):
		
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
                
                for (d1,d2) in ((2,1),(-2,-1),(2,-1),(-2,1),(1,2),(-1,-2),(-1,2),(1,-2)):
                        if self.inside(i+d1,j+d2):	
                                if board[x][y]!='0' and not color in board[i+d1][j+d2] and 'h' in board[i+d1][j+d2]:
                                        return False
                if color=='B':
                        c=1
                else:
                        c=-1
                for (d1,d2) in ((c,1),(c,-1)):
                        if self.inside(i+d1,j+d2):	
                                if board[x][y]!='0' and not color in board[i+d1][j+d2] and 'p' in board[i+d1][j+d2]:
                                        return False
                for (d1,d2) in ((-1,-1),(1,-1),(-1,1),(1,1),(0,1),(1,0),(0,-1),(-1,0)):
                        if self.inside(i+d1,j+d2):	
                                if board[x][y]!='0' and not color in board[i+d1][j+d2] and 'a' in board[i+d1][j+d2]:
                                        return False
                return True

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

        def isCheckMate(self,board,colour):
                moves=[]
                for i in range(8):
                        for j in range(8):
                                if colour in board[i][j]:
                                        moves.extend(self.getValidMoves(board,(i,j)))
                if len(moves)==0:
                        return True
                else:
                        return False
                                                                  
        def isValid(self,board,colour,fromTuple,toTuple):
                validMoves=self.getValidMoves(board,fromTuple)
                if (toTuple in validMoves) and self.isKingInCheck(board,colour,fromTuple,toTuple):
                        return True
                else:
                        return False
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
                                if fromRow==1 and self.isClear(board,fromMoveTuple,(3,fromColumn))==True and board[3][fromColumn]=='0':
                                        singleMove=(3,fromColumn)
                                        validMoveTuple.append(singleMove)
                                if fromColumn!=0 and fromRow!=7 and 'W' in board[fromRow+1][fromColumn-1]:
                                    singleMove=(fromRow+1,fromColumn-1)
                                    validMoveTuple.append(singleMove)
                                if fromColumn!=7 and fromRow!=7 and 'W' in board[fromRow+1][fromColumn+1]:
                                    singleMove=(fromRow+1,fromColumn+1)
                                    validMoveTuple.append(singleMove)
                                if board[fromRow+1][fromColumn]=='0':
                                    singleMove=(fromRow+1,fromColumn)
                                    validMoveTuple.append(singleMove)
                        if 'W' in ch:
                                if fromRow==6 and self.isClear(board,fromMoveTuple,(4,fromColumn))==True and board[4][fromColumn]=='0':
                                        singleMove=(4,fromColumn)
                                        validMoveTuple.append(singleMove)
                                if fromColumn!=0 and fromRow!=0 and 'B' in board[fromRow-1][fromColumn-1]:
                                    singleMove=(fromRow-1,fromColumn-1)
                                    validMoveTuple.append(singleMove)
                                if fromColumn!=7 and fromRow!=0 and 'B' in board[fromRow-1][fromColumn+1]:
                                    singleMove=(fromRow-1,fromColumn+1)
                                    validMoveTuple.append(singleMove)
                                if board[fromRow-1][fromColumn]=='0':
                                    singleMove=(fromRow-1,fromColumn)
                                    validMoveTuple.append(singleMove)
                if 'r' in ch:   #For Rook
                        for i in range(8):
                                if i==fromRow:
                                    pass
                                elif self.isMyPiece(board,i,fromColumn,colour)==False and self.isClear(board,fromMoveTuple,(i,fromColumn))==True:
                                    singleMove=(i,fromColumn)
                                    validMoveTuple.append(singleMove)
                        for j in range(8):
                                if j==fromColumn:
                                    pass
                                elif self.isMyPiece(board,fromRow,j,colour)==False and self.isClear(board,fromMoveTuple,(fromRow,j))==True:
                                    singleMove=(fromRow,j)
                                    validMoveTuple.append(singleMove)
                if 'b' in ch:    #For bishop
                        for i in range(8):
                                for j in range(8):
                                        if abs(i-fromRow)==abs(j-fromColumn) and self.isMyPiece(board,i,j,colour)==False and self.isClear(board,fromMoveTuple,(i,j))==True:
                                                if i==fromRow and j==fromColumn:
                                                        continue
                                                else:
                                                        singleMove=(i,j)
                                                        validMoveTuple.append(singleMove)
                if 'a' in ch:    #For king
                        for i in range(8):
                                for j in range(8):
                                        if self.isMyPiece(board,i,j,colour)==False:
                                                if i==fromRow:
                                                        if j==fromColumn+1 or j==fromColumn-1:
                                                                singleMove=(i,j)
                                                                validMoveTuple.append(singleMove)
                                                if j==fromColumn:
                                                        if i==fromRow+1 or i==fromRow-1:
                                                                singleMove=(i,j)
                                                                validMoveTuple.append(singleMove)
                                                if i==fromRow+1:
                                                        if j==fromColumn-1 or j==fromColumn+1:
                                                                singleMove=(i,j)
                                                                validMoveTuple.append(singleMove)
                                                if i==fromRow-1:
                                                        if j==fromColumn+1 or j==fromColumn-1:
                                                                singleMove=(i,j)
                                                                validMoveTuple.append(singleMove)

                if 'q' in ch:         #For Queen
                        for i in range(8):
                                if i==fromRow:
                                    continue
                                elif self.isMyPiece(board,i,fromColumn,colour)==False and self.isClear(board,fromMoveTuple,(i,fromColumn))==True:
                                    singleMove=(i,fromColumn)
                                    validMoveTuple.append(singleMove)
                        for j in range(8):
                                if j==fromColumn:
                                    continue
                                elif self.isMyPiece(board,fromRow,j,colour)==False and self.isClear(board,fromMoveTuple,(fromRow,j))==True:
                                    singleMove=(fromRow,j)
                                    validMoveTuple.append(singleMove)
                        for i in range(8):
                                for j in range(8):
                                        if abs(i-fromRow)==abs(j-fromColumn) and self.isMyPiece(board,i,j,colour)==False and self.isClear(board,fromMoveTuple,(i,j))==True:
                                                if i==fromRow and j==fromColumn:
                                                        pass
                                                else:
                                                        singleMove=(i,j)
                                                        validMoveTuple.append(singleMove)


                if 'h' in ch:             #For KNIGHT
                        for i in range(8):
                                for j in range(8):
                                        if self.isMyPiece(board,i,j,colour)==False:
                                                if i==fromRow+2 or i==fromRow-2:
                                                        if j==fromColumn-1 or j==fromColumn+1:
                                                                singleMove=(i,j)
                                                                validMoveTuple.append(singleMove)
                                                if j==fromColumn+2 or j==fromColumn-2:
                                                        if i==fromRow+1 or i==fromRow-1:
                                                                singleMove=(i,j)
                                                                validMoveTuple.append(singleMove)
                validMoves=[]
                king=colour+'a'
                for i in range(8):
                        for j in range(8):
                                if king in board[i][j]:
                                        (x,y)=(i,j)
                                        break
                for move in validMoveTuple:
                        c=board[move[0]][move[1]]
                        board[move[0]][move[1]]=ch
                        board[fromRow][fromColumn]='0'
                        if 'a' in ch:
                                (x,y)=(move[0],move[1])
                        if self.safe(x,y,board,colour):
                                validMoves.append(move)
                        board[move[0]][move[1]]=c
                        board[fromRow][fromColumn]=ch
                return validMoves

'''board=[['Br','Bh','Bb','0','Bq','Bb','Bh','Br'],
       ['Bp','Bp','Bp','0','Bp','Bp','Bp','Bp'],
       ['0','0','Wr','0','0','0','0','0'],
       ['0','0','Wr','0','Ba','0','0','0'],
       ['0','Wq','0','0','0','0','0','0'],
       ['0','0','0','0','0','0','0','0'],
       ['Wp','Wp','Wp','Wp','Wp','Wp','Wp','Wp'],
       ['Wr','Wh','Wb','Wa','0','Wb','Wh','Wr']]
ob=Rules()
valid=ob.getValidMoves(board,(4,1))
print(valid)
check=ob.isKingInCheck(board,'B',(3,4),(4,4))
print(check)
checkMate=ob.isCheckMate(board,'B')
print(checkMate)
'''
