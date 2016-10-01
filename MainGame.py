from Rules import Rules
from ChessBoard import ChessBoard
from Screen1 import Screen
class MainGame():
    def __init__(self):
        self.Board=ChessBoard()
        self.ChessRules=Rules()
        self.DisplayScreen=Screen()
        
    def Game(self):
        print ("Let's Play Chess!")
        board1=[['Br','Bh','Bb','Ba','Bq','Bb','Bh','Br'],
                ['Bp','Bp','Bp','Bp','Bp','Bp','Bp','Bp'],
                ['0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0'],
                ['Wp','Wp','Wp','Wp','Wp','Wp','Wp','Wp'],
                ['Wr','Wh','Wb','Wa','Wq','Wb','Wh','Wr']]
        '''board1=[['0','0','0','0','0','Bb','Bh','Br'],
                ['Bp','Bp','Bp','Bp','Bp','Bp','Bp','Bp'],
                ['0','0','0','0','0','0','Wr','0'],
                ['0','0','0','0','Ba','0','0','0'],
                ['0','Wq','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','Wr','0'],
                ['Wp','Wp','Wp','Wp','Wp','Wp','Wp','Wp'],
                ['Wr','Wh','Wb','Wa','Wq','Wb','Wh','Wr']]'''
        self.DisplayScreen.play(board1)
ob=MainGame()
ob.Game()
