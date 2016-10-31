from Rules import Rules
from ChessBoard import ChessBoard
from Screen1 import Screen
from GUI import GUI
from minmax import minmax
class MainGameGUI:
    def __init__(self):
        self.cb=ChessBoard()
        self.cr=Rules()
        self.gui=GUI()
        self.ai=minmax()
        self.player=['W','B']

    def mainloop(self,board):
        currentPlayerIndex = 0
        while not self.cr.isCheckMate(board,self.player[currentPlayerIndex]):
            currentColor = self.player[currentPlayerIndex]
            if currentColor == 'W':
                name="White"
            else:
                name="Black"
            self.gui.draw(board)
            if self.cr.isKingInCheck(board,currentColor):
                    print name+" is in check"

            if currentColor=='B':
                d = self.ai.alphabeta(board,'B',3,-99999999,999999999)
                moveTuple=d[1]
            else:
                moveTuple = self.gui.getPlayerInput(board,currentColor)
            moveReport = self.cb.makeMove(board,moveTuple)
            currentPlayerIndex = (currentPlayerIndex+1)%2
        if name=="White":
            name1="Black"
        else:
            name1="White"
        print name1+" lost"
        winnerIndex = (currentPlayerIndex+1)%2
        currentColor=self.player[winnerIndex]
        if currentColor == 'W':
            name="White"
        else:
            name="Black"
        self.gui.EndGame(board)
board=  [['Br','Bh','Bb','Bq','Ba','Bb','Bh','Br'],
        ['Bp','Bp','Bp','Bp','Bp','Bp','Bp','Bp'],
        ['0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0'],
        ['Wp','Wp','Wp','Wp','Wp','Wp','Wp','Wp'],
        ['Wr','Wh','Wb','Wq','Wa','Wb','Wh','Wr']]
ob=MainGameGUI()
ob.mainloop(board)
