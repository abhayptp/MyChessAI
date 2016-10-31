from ChessBoard import ChessBoard
from Rules import Rules
class Evaluation:
    def __init__(self):
        self.cb=ChessBoard()
        self.rs=Rules()
        self.value={'Bp':-1,'Wp':1,'Br':-3,'Wr':3,'Bh':-2,'Wh':2,'Bb':-4,'Wb':4,'Wq':8,'Bq':-8,'Wa':10,'Ba':-10,'0':0}

    
    def evaluate(self,board):
        eval=0
        for i in range(8):
            for j in range(8):
                eval=eval+self.value[board[i][j]]
        return eval

    
