from ChessBoard import ChessBoard
from Rules import Rules
class Evaluation:
    def __init__(self):
        self.cb=ChessBoard()
        self.cr=Rules()
        #To store the white and black king pos
        self.wk=[]
        self.bk=[]
        self.wForce=[]
        self.bForce=[]
        
    #To evaluate board position
    def evaluate(self,board):
        
        wValue=0
        bValue=0
        self.wForce=self.cb.getForce('W',board)
        self.bForce=self.cb.getForce('B',board)
        for pos in self.wForce:
            if board[pos[0]][pos[1]]=='Wa':
                self.wk=pos
        for pos in self.bForce:
            if board[pos[0]][pos[1]]=='Ba':
                self.bk=pos
        for pos in self.wForce:
            if board[pos[0]][pos[1]]=='Wp':
                wValue = wValue + 150 + self.getPValue(board,pos)
            elif board[pos[0]][pos[1]]=='Wr':
                wValue = wValue + 514 + self.getRookValue(board,pos)
            elif board[pos[0]][pos[1]]=='Wb':
                wValue = wValue + 442 + self.getBishopValue(board,pos)
            elif board[pos[0]][pos[1]]=='Wh':
                wValue = wValue + 384 + self.getKnightValue(board,pos)
            elif board[pos[0]][pos[1]]=='Wq':
                wValue = wValue + 1000
            else:
                wValue = wValue + self.getKingValue(board,pos)
                
        for pos in self.bForce:
            if board[pos[0]][pos[1]]=='Bp':
                bValue = bValue + 150 + self.getPValue(board,pos)
            elif board[pos[0]][pos[1]]=='Br':
                bValue = bValue + 514 + self.getRookValue(board,pos)
            elif board[pos[0]][pos[1]]=='Bb':
                bValue = bValue + 442 + self.getBishopValue(board,pos)
            elif board[pos[0]][pos[1]]=='Bh':
                bValue = bValue + 384 + self.getKnightValue(board,pos)
            elif board[pos[0]][pos[1]]=='Bq':
                bValue = bValue + 1000
            else:
                 bValue = bValue + self.getKingValue(board,pos)

        value=wValue-bValue
        return value

    def getPValue(self,board,(r,c)):
        pawnValue = 0
        #To promote pawn promotion
        if 'B' in board[r][c]:
            if r==7:
                pawnValue = pawnValue+595
            
            elif r==6:
                if board[r+1][c]=='0':
                    pawnValue = pawnValue + 213
                else:
                    pawnValue = pawnValue + 54
            elif r==5 :
		if board[r+1][c]=='0' and board[r+2][c]=='0' :
		    pawnValue = pawnValue + 213
		else :
		    pawnValue = pawnValue + 117
	    elif r==4 :
		pawnValue = pawnValue + 53
	    else :
                pass
            #To check for blocked pawn
            if r!=7 and r>0:
                if board[r+1][c]!='0':
                    pawnValue = pawnValue - 51
        if 'W' in board[r][c]:
            #To promote pawn promotion
            if r==0:
                pawnValue=pawnValue+595
            
            elif r==1:
                if board[r-1][c]=='0':
                    pawnValue = pawnValue + 213
                else:
                    pawnValue = pawnValue + 54
            elif r==2 :
		if board[r-1][c]=='0' and board[r-2][c]=='0' :
		    pawnValue = pawnValue + 213
		else :
		    pawnValue = pawnValue + 117
	    elif r==3 :
		pawnValue = pawnValue + 53
	    else :
                pass
            #To check for blocked pawn
            if r!=0 and r<7:
                if board[r-1][c]!='0':
                    pawnValue = pawnValue - 51

        return pawnValue
    
    def getRookValue(self,board,(r,c)):
        rookValue=0
        if r>0 and r<7 and c>0 and c<7:
                rookValue = rookValue + 100
        #To make the king safe
        if 'W' in board[r][c]:
		if abs(self.bk[0] - r) <= 1 or abs(self.bk[1] - c) <= 1 :
			rookValue = rookValue + 57
	if 'B' in board[r][c]:
		if abs(self.wk[0] - r) <= 1 or abs(self.wk[1] - c) <= 1 :
			rookValue = rookValue + 57
	return rookValue

    def getKnightValue(self,board,(r,c)):
        knightValue=0
        #To attack the opposite king
        if 'W' in board[r][c]:
            distance = abs(r - self.bk[0]) + abs(c - self.bk[1])
            if distance <= 2 :
                    knightValue = knightValue + 98
            elif distance <= 4 :
                    knightValue = knightValue + 48
            else :
                pass
        if 'B' in board[r][c]:
            distance = abs(r - self.wk[0]) + abs(c - self.wk[1])
            if distance <= 2 :
                if len(self.wForce)==1:
                    knightValue = knightValue + 267
                else:
                    knightValue = knightValue + 98
            elif distance <= 4 :
                if len(self.wForce)==1:
                    knightValue = knightValue + 167
                else:
                    knightValue = knightValue + 51
            else :
                pass
        return knightValue

    def getBishopValue(self,board,(r,c)):
        bishopValue=0
        #To attack the opposite king
        if 'W' in board[r][c]:
            distance = abs(r - self.bk[0]) + abs(c - self.bk[1])
            if distance <= 2 :
                    bishopValue = bishopValue+ 50
            elif distance <= 4 :
                    bishopValue = bishopValue + 24
            else :
                pass
        if 'B' in board[r][c]:
            distance = abs(r-self.wk[0]) + abs(c-self.wk[1])
            if distance <=2 :
                if len(self.wForce)==1:
                    bishopValue = bishopValue + 250
                else:
                    bishopValue = bishopValue + 50
            elif distance<=4 :
                if len(self.wForce)==1:
                    bishopValue = bishopValue + 193
                else:
                    bishopValue = bishopValue + 42
            else:
                pass
        return bishopValue
    
    def getKingValue (self,board,(r, c)):
	kingValue = 0
        if r == 7 and (c <= 1 or c >= 6) :
                kingValue = kingValue + 50
	ch=board[r][c][0]
	#To make the king safe
	if ch in board[r][c] :
		if self.cr.inside(r,c-1) :
			if ch in board[r][c-1] :
				kingValue = kingValue + 16
		if self.cr.inside(r-1,c-1) :
			if ch in board[r-1][c-1] :
				kingValue = kingValue + 13
		if self.cr.inside(r+1,c) :
			if ch in board[r+1][c] :
				kingValue = kingValue + 14
		if self.cr.inside(r+1,c+1) :
			if ch in board[r+1][c+1] :
				kingValue = kingValue + 17
		if self.cr.inside(r,c+1) :
			if ch in board[r][c+1] :
				kingValue = kingValue + 11
		if self.cr.inside(r-1,c+1) :
			if ch in board[r-1][c+1] :
				kingValue = kingValue + 17
		if self.cr.inside(r-1,c) :
			if ch in board[r-1][c] :
				kingValue = kingValue + 14
		if self.cr.inside(r-1,c-1) :
			if ch in board[r-1][c-1] :
				kingValue = kingValue + 12
	
        return kingValue 

            
        
