from Rules import Rules
import random
class ChessAI:	
    def __init__(self):
        self.ChessRule=Rules()
    def getMove(self,board,color):
        myPieces = self.getMyPiecesWithValidMoves(board,color)
        fromTuple = myPieces[random.randint(0,len(myPieces)-1)]
        legalMove = self.getLegalMoves(board,fromTuple)
        toTuple = legalMove[random.randint(0,len(legalMove)-1)]
        moveTuple = (fromTuple,toTuple)
        return moveTuple
            
    def getMyPiecesWithValidMoves(self,board,color):
        myColor = 'B'
        enemyColor = 'W'
        myPieces = []
        for row in range(8):
                for col in range(8):
                        piece = board[row][col]
                        if myColor in piece:
                                if len(self.getLegalMoves(board,(row,col))) > 0:
                                        myPieces.append((row,col))	
        
        return myPieces

    def getLegalMoves(self,board,(row,col)):
        moves=self.ChessRule.getValidMoves(board,(row,col))
        legalMoves=[]
        for move in moves:
            if self.ChessRule.isKingInCheck(board,'B',(row,col),move)==False:
                legalMoves.append(move)
        return legalMoves
