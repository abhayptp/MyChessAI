from Rules import Rules
from ChessBoard import ChessBoard
from Evaluation import Evaluation
import math
class minmax:
    def __init__(self):
        self.cr=Rules()
        self.cb=ChessBoard()
        self.ev=Evaluation()

    def makeCopy(self,board):
        return [[board[j][i] for i in range(8)] for j in range(8)]

    def makeMove(self,board,(i,j),(p,q)):
        board[p][q]=board[i][j]
        board[i][j]='0'
        return board

    def legal_moves(self,colour,board):
        p=self.cb.getForce(colour,board)
        m=[]
        for pos in p:
            to=self.cr.getValidMoves(board,pos)
            for x in to:
                m.append((pos,x))
        return m

    def alphabeta(self,position, to_move, depth, alpha, beta):
        if depth == 0 or self.cr.isCheckMate(position,'W') or self.cr.isCheckMate(position,'B'):
            q=self.ev.evaluate(position)
            return (q, None)
        else: 
            if to_move == 'W':
                bestmove = None
                for move1 in self.legal_moves('W',position):
                    position1=self.makeCopy(position)
                    new_position = self.makeMove(position1, move1[0],move1[1])
                    (score, move) = self.alphabeta(new_position, "black", depth - 1, alpha, beta)
                    if score > alpha: # white maximizes her score
                        alpha = score
                        bestmove = move1
                        if alpha >= beta: # alpha-beta cutoff
                            break
                return (alpha, bestmove)
            else:
                bestmove = None
                for move1 in self.legal_moves('B',position):
                    position1=self.makeCopy(position)
                    new_position = self.makeMove(position1, move1[0], move1[1])
                    (score, move) = self.alphabeta(new_position, 'W', depth-1, alpha, beta)
                    if score < beta: # black minimizes his score
                        beta = score
                        bestmove = move1
                        if alpha >= beta: # alpha-beta cutoff
                            break
                return (beta, bestmove)


        
'''ob=minmax()
board1=[['Br','Bh','Bb','Ba','Bq','Bb','Bh','Br'],
       ['Bp','Bp','Bp','0','Bp','Bp','Bp','Bp'],
       ['0','0','Wr','0','0','0','0','0'],
       ['0','0','Wr','0','0','0','0','0'],
       ['0','Wq','0','0','0','0','0','0'],
       ['0','0','0','0','0','0','0','0'],
       ['Wp','Wp','Wp','Wp','Wp','Wp','Wp','Wp'],
       ['Wr','Wh','Wb','Wa','0','Wb','Wh','Wr']]
c=ob.alphabeta(board1,'B',5,-99999999,999999999)
print c
'''
