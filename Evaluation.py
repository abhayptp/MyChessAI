from ChessBoard import ChessBoard
from Rules import Rules
class Evaluation:
    def __init__(self):
        self.cb=ChessBoard()
        self.rs=Rules()
        self.value={'Bp':-1,'Wp':1,'Br':-2,'Wr':2,'Bh':-3,'Wh':3,'Bb':-4,'Wb':4,'Wq':5,'Bq':-5,'Wa':6,'Ba':-6,'0':0}

    
    def evaluate(self,board):
        eval=0
        for i in range(8):
            for j in range(8):
                eval=eval+self.value[board[i][j]]
        return eval

    
