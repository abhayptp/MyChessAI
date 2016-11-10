from Rules import Rules
from ChessBoard import ChessBoard
from Evaluation import Evaluation
import math
class minmax:
    def __init__(self):
        self.cr=Rules()
        self.cb=ChessBoard()
        self.ev=Evaluation()
        self.count=0;

    #It gets the move by minmax search(with alpha beta pruning)
    def getMove(self,board,colour):
        if colour=='W':
            d=self.alphabeta(board,colour,1,-999999,999999)
        else:
            d=self.alphabeta(board,colour,3,-999999,999999)
        moveTuple=d[1]
        return moveTuple

    #For making the copy of the board so that the changes are not reflected in the original board
    def makeCopy(self,board):
        return [[board[j][i] for i in range(8)] for j in range(8)]

    #To make the move in the board for the subsequent depth
    def makeMove(self,board,(i,j),(p,q)):
        board[p][q]=board[i][j]
        board[i][j]='0'
        return board

    #To return all the legal moves
    def legal_moves(self,colour,board):
        p=self.cb.getForce(colour,board)
        m=[]
        for pos in p:
            to=self.cr.getValidMoves(board,pos)
            for x in to:
                m.append((pos,x))
        return m

    #Main minmax serch with alpha beta pruning
    def alphabeta(self,position, to_move, depth, alpha, beta):
        #If depth=0, evaluate the board
        if depth == 0:
            q=self.ev.evaluate(position)
            self.count=self.count+1;
            return (q, None)
        elif self.cr.isCheckMate(position,'W'):
            return (100000,None)
        elif self.cr.isCheckMate(position,'B'):
            return (-100000,None)
        else:
            #Scores are evaluated with respect to white. So, White maximizes it and black minimizes it
            if to_move == 'W':
                bestmove = None
                for move1 in self.legal_moves('W',position):
                    #Making the copy of the board so that the changes are not reflected in the original board
                    position1=self.makeCopy(position)
                    new_position = self.makeMove(position1, move1[0],move1[1])
                    (score, move) = self.alphabeta(new_position, 'B', depth - 1, alpha, beta)
                    if score > alpha: # white maximizes white's score
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
                    if score < beta: # black minimizes white's score
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
