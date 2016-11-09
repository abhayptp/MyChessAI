from ChessBoard import ChessBoard
from Rules import Rules
class Evaluation:
    def __init__(self):
        self.cb=ChessBoard()
        self.cr=Rules()
        self.wk=[]
        self.bk=[]
    
    def evaluate(self,board):
        wForce=self.cb.getForce('W',board)
        bForce=self.cb.getForce('B',board)
        wValue=0
        bValue=0
        for pos in wForce:
            if board[pos[0]][pos[1]]=='Wa':
                self.wk=pos
        for pos in bForce:
            if board[pos[0]][pos[1]]=='Ba':
                self.bk=pos
        for pos in wForce:
            if board[pos[0]][pos[1]]=='Wp':
                wValue = wValue + 100
                wValue = wValue + self.getPValue(board,pos)
            elif board[pos[0]][pos[1]]=='Wr':
                wValue = wValue + 500
                wValue = wValue + self.getRookValue(board,pos)
            elif board[pos[0]][pos[1]]=='Wb':
                wValue = wValue + 400
                wValue = wValue + self.getBishopValue(board,pos)
            elif board[pos[0]][pos[1]]=='Wh':
                wValue = wValue + 300
                wValue = wValue + self.getKnightValue(board,pos)
            elif board[pos[0]][pos[1]]=='Wq':
                wValue = wValue + 1000
                wValue = wValue + self.getKingValue(board,pos)
            else:
                pass
                
        for pos in bForce:
            if board[pos[0]][pos[1]]=='Bp':
                bValue = wValue + 100
                wValue = bValue + self.getPValue(board,pos)
            elif board[pos[0]][pos[1]]=='Br':
                bValue = wValue + 500
                bValue = bValue + self.getRookValue(board,pos)
            elif board[pos[0]][pos[1]]=='Bb':
                bValue = wValue + 400
                bValue = bValue + self.getBishopValue(board,pos)
            elif board[pos[0]][pos[1]]=='Bh':
                bValue = wValue + 300
                bValue = bValue + self.getKnightValue(board,pos)
            elif board[pos[0]][pos[1]]=='Bq':
                bValue = wValue + 1000
                bValue = bValue + self.getKingValue(board,pos)
            else:
                pass
        value=wValue-bValue
        return value

    def getPValue(self,board,(r,c)):
        pawnValue = 0
        if 'W' in board[r][c]:
            if r==6:
                if board[r-1][c]=='0':
                    pawnValue = pawnValue + 500
                else:
                    pawnValue = pawnValue + 300
            elif r==5 :
		if board[r-1][c]=='0' and board[r-2][c]=='0' :
		    pawnValue = pawnValue + 200
		else :
		    pawnValue = pawnValue + 100
	    elif r==4 :
		pawnValue = pawnValue + 50
	    else :
                pass
            if r!=7:
                if board[r-1][c]!='0':
                    pawnValue = pawnValue - 50
        if 'B' in board[r][c]:
            if r==1:
                if board[r+1][c]=='0':
                    pawnValue = pawnValue + 500
                else:
                    pawnValue = pawnValue + 300
            elif r==2 :
		if board[r+1][c]=='0' and board[r+2][c]=='0' :
		    pawnValue = pawnValue + 200
		else :
		    pawnValue = pawnValue + 100
	    elif r==3 :
		pawnValue = pawnValue + 50
	    else :
                pass
            if r!=0:
                if board[r+1][c]!='0':
                    pawnValue = pawnValue - 50

        return pawnValue
    def getRookValue(self,board,(r,c)):
        rookValue=0
        if r>0 and r<7 and c>0 and c<7:
                rookValue = rookValue + 100
        if 'W' in board[r][c]:
		if abs(self.wk[0] - r) <= 1 or abs(self.wk[1] - c) <= 1 :
			rookValue = rookValue + 50
	if 'B' in board[r][c]:
		if abs(self.bk[0] - r) <= 1 or abs(self.bk[1] - c) <= 1 :
			rookValue = rookValue + 50
	return rookValue

    def getKnightValue(self,board,(r,c)):
        knightValue=0
        if 'W' in board[r][c]:
            distance = abs(r - self.bk[0]) + abs(c - self.bk[1])
            if distance <= 2 :
                knightValue = knightValue + 100
            elif distance <= 4 :
                knightValue = knightValue + 50
            else :
                pass
        elif 'B' in board[r][c]:
            distance = abs(r - self.wk[0]) + abs(c - self.wk[1])
            if distance <= 2 :
                knightValue = knightValue + 100
            elif distance <= 4 :
                knightValue = knightValue + 50
            else :
                pass
        return knightValue

    def getBishopValue(self,board,(r,c)):
        bishopValue=0
        if 'W' in board[r][c]:
            distance = abs(r - self.bk[0]) + abs(c - self.bk[1])
            if distance <= 2 :
                    bishopValue = bishopValue+ 100
            elif distance <= 4 :
                    bishopValue = bishopValue + 50
            else :
                pass
        if 'B' in board[r][c]:
            distance = abs(r-self.wk[0]) + abs(c-self.wk[1])
            if distance <=2 :
                bishopValue = bishopValue + 100
            elif distance<=4 :
                bishopValue = bishopValue + 50
            else:
                pass
        return bishopValue
    def getKingValue (self,board,(r, c)):
	kingValue = 0
        if r == 7 and (c <= 1 or c >= 6) :
                kingValue += 50
	ch=board[r][c][0]
	if ch in board[r][c] :
		if self.cr.inside(r,c-1) :
			if ch in board[r][c-1] :
				kingValue = kingValue + 20
		if self.cr.inside(r-1,c-1) :
			if ch in board[r-1][c-1] :
				kingValue = kingValue + 20
		if self.cr.inside(r+1,c) :
			if ch in board[r+1][c] :
				kingValue = kingValue + 20
		if self.cr.inside(r+1,c+1) :
			if ch in board[r+1][c+1] :
				kingValue = kingValue + 20
		if self.cr.inside(r,c+1) :
			if ch in board[r][c+1] :
				kingValue = kingValue + 20
		if self.cr.inside(r-1,c+1) :
			if ch in board[r-1][c+1] :
				kingValue = kingValue + 20
		if self.cr.inside(r-1,c) :
			if ch in board[r-1][c] :
				kingValue = kingValue + 20
		if self.cr.inside(r-1,c-1) :
			if ch in board[r-1][c-1] :
				kingValue = kingValue + 20
	
        return kingValue 

            
        
