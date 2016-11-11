#This is the driver function which runs the chess.
#In this game, the player will be white and ai will be black.
#And black is up in the board.
from __future__ import print_function
from Rules import Rules
from ChessBoard import ChessBoard
from Screen1 import Screen
from GUI import GUI
from minmax import minmax
from GameSetup import GameSetup
from ChessAI import ChessAI
class MainGameGUI:
    def __init__(self):
        self.cb=ChessBoard()
        self.cr=Rules()
        self.gui=GUI()
        #To check which player has to move
        self.player=['W','B']
        self.moves=0
        
        self.ai2=ChessAI()
        
        self.pieces=0
        GameParams = GameSetup()
        (player1Name, player1Color, player1Type, player2Name, player2Color, player2Type) = GameParams.getGameInfo()
        if player2Type=='randomAI':
            self.ai=ChessAI()
        elif player2Type=='minmaxAI':
            self.ai=minmax()
        else:
            self.ai=self.gui

    def mainloop(self,board):
        currentPlayerIndex = 0
        self.pieces=0
        depth=3
        draw=0
        #Game will continue until there is a checkmate to black or white.
        while not self.cr.isCheckMate(board,self.player[currentPlayerIndex]):
            currentColor = self.player[currentPlayerIndex]
            if currentColor == 'W':
                name="White"
            else:
                name="Black"
            #For drawing the board with the help of gui function
            self.gui.draw(board)
            #For warning the other player if there is a check
            if self.cr.isKingInCheck(board,currentColor):
                    print("%s is in check"%name)

            if currentColor=='B':
                #Getting the best move searched by minmax(with alpha-beta pruning) algo
                moveTuple = self.ai.getMove(board,'B',depth)
                #As the value is also returned, so taking only d[1]
                #print "Black"
                #print(self.ai.count)
                #self.ai.count=0;
                if moveTuple==None:
                    self.ai2.getMove(board,'B')
                self.moves=self.moves+1
                if self.moves>100:
                    draw=1
                    break
            else:
                #Else getting the move from player
                moveTuple = self.gui.getMove(board,'W')
            moveReport = self.cb.makeMove(board,moveTuple)
            currentPlayerIndex = (currentPlayerIndex+1)%2
        if draw==1:    
            if name=="White":
                name1="Black"
            else:
                name1="White"
            #Printing that the player lost(as checkmate has been done)
            print("%s lost"%name1)
            #print("Moves= %d"%self.moves)
            self.gui.draw(board)
            #Ends the game
        else:
            print("Draw")
        #Ends the game
        self.gui.endGame(board)
board=  [['Br','Bh','Bb','Bq','Ba','Bb','Bh','Br'],
        ['Bp','Bp','Bp','Bp','Bp','Bp','Bp','Bp'],
        ['0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0'],
        ['Wp','Wp','Wp','Wp','Wp','Wp','Wp','Wp'],
        ['Wr','Wh','Wb','Wq','Wa','Wb','Wh','Wr']]
ob=MainGameGUI()
ob.mainloop(ob.cb.board)
