import pygame,sys
import os
from pygame.locals import *
from Rules import Rules
from ChessBoard import ChessBoard
class GUI:
    def __init__(self):
        pygame.init()
        pygame.display.init()
        self.screen=pygame.display.set_mode((500,500))
        pygame.display.set_caption("My Chess")
        self.boardStart_x = 50
        self.boardStart_y = 50
        self.loadImages()
        self.fontDefault = pygame.font.Font( None, 20 )
        self.Rules=Rules()
        self.cb=ChessBoard()

    def loadImages(self):
        self.square_size = 50
        self.white_square = pygame.image.load(os.path.join("images","white_square.png")).convert()
        self.brown_square = pygame.image.load(os.path.join("images","Brown.png")).convert()
        self.cyan_square = pygame.image.load(os.path.join("images","cyan_square.png")).convert()
        self.black_pawn = pygame.image.load(os.path.join("images","BlackPawn.png")).convert()
        self.black_pawn = pygame.transform.scale(self.black_pawn, (self.square_size,self.square_size))
        self.black_rook = pygame.image.load(os.path.join("images","BlackRook.png")).convert()
        self.black_rook = pygame.transform.scale(self.black_rook, (self.square_size,self.square_size))
        self.black_bishop = pygame.image.load(os.path.join("images","BlackBishop.png")).convert()
        self.black_bishop = pygame.transform.scale(self.black_bishop, (self.square_size,self.square_size))
        self.black_knight = pygame.image.load(os.path.join("images","BlackKnight.png")).convert()
        self.black_knight = pygame.transform.scale(self.black_knight, (self.square_size,self.square_size))
        self.black_queen = pygame.image.load(os.path.join("images","BlackQueen.png")).convert()
        self.black_queen = pygame.transform.scale(self.black_queen, (self.square_size,self.square_size))
        self.black_king = pygame.image.load(os.path.join("images","BlackKing.png")).convert()
        self.black_king = pygame.transform.scale(self.black_king, (self.square_size,self.square_size))
        self.white_pawn = pygame.image.load(os.path.join("images","WhitePawn.png")).convert()
        self.white_pawn = pygame.transform.scale(self.white_pawn, (self.square_size,self.square_size))
        self.white_rook = pygame.image.load(os.path.join("images","WhiteRook.png")).convert()
        self.white_rook = pygame.transform.scale(self.white_rook, (self.square_size,self.square_size))
        self.white_bishop = pygame.image.load(os.path.join("images","WhiteBishop.png")).convert()
        self.white_bishop = pygame.transform.scale(self.white_bishop, (self.square_size,self.square_size))
        self.white_knight = pygame.image.load(os.path.join("images","WhiteKnight.png")).convert()
        self.white_knight = pygame.transform.scale(self.white_knight, (self.square_size,self.square_size))
        self.white_queen = pygame.image.load(os.path.join("images","WhiteQueen.png")).convert()
        self.white_queen = pygame.transform.scale(self.white_queen, (self.square_size,self.square_size))
        self.white_king = pygame.image.load(os.path.join("images","WhiteKing.png")).convert()
        self.white_king = pygame.transform.scale(self.white_king, (self.square_size,self.square_size))

    def convertToScreen(self,squareTuple):
        (row,col) = squareTuple
        screenX = self.boardStart_x + col*self.square_size
        screenY = self.boardStart_y + row*self.square_size
        return (screenX,screenY)
		
    def convertToChess(self,screenTuple):
        (X,Y) = screenTuple
        row = (Y-self.boardStart_y) / self.square_size
        col = (X-self.boardStart_x) / self.square_size
        return (row,col)
            
            
    def draw(self,board,highlightSquares=[]):
        self.screen.fill((0,0,0))
        boardSize = 8
        current_square = 0
        for r in range(boardSize):
            for c in range(boardSize):
                (screenX,screenY) = self.convertToScreen((r,c))
                if current_square:
                    self.screen.blit(self.brown_square,(screenX,screenY))
                    current_square = (current_square+1)%2
                else:
                    self.screen.blit(self.white_square,(screenX,screenY))
                    current_square = (current_square+1)%2

            current_square = (current_square+1)%2
        chessboard_obj = ChessBoard(0)
        color = (255,255,255)
        antialias = 1
        
        for c in range(boardSize):
            for r in [-1,boardSize]:
                (screenX,screenY) = self.convertToScreen((r,c))
                screenX = screenX + self.square_size/2
                screenY = screenY + self.square_size/2
                notation = self.cb.convertToAlgebraicNotation_col(c)
                renderedLine = self.fontDefault.render(notation,antialias,color)
                self.screen.blit(renderedLine,(screenX,screenY))
        
        for r in range(boardSize):
            for c in [-1,boardSize]:
                (screenX,screenY) = self.convertToScreen((r,c))
                screenX = screenX + self.square_size/2
                screenY = screenY + self.square_size/2
                notation = self.cb.convertToAlgebraicNotation_row(r)
                renderedLine = self.fontDefault.render(notation,antialias,color)
                self.screen.blit(renderedLine,(screenX,screenY))
                        
        for square in highlightSquares:
            (screenX,screenY) = self.convertToScreen(square)
            self.screen.blit(self.cyan_square,(screenX,screenY))
        
        for r in range(boardSize):
            for c in range(boardSize):
                (screenX,screenY) = self.convertToScreen((r,c))
                if board[r][c] == 'Bp':
                        self.screen.blit(self.black_pawn,(screenX,screenY))
                if board[r][c] == 'Br':
                        self.screen.blit(self.black_rook,(screenX,screenY))
                if board[r][c] == 'Bh':
                        self.screen.blit(self.black_knight,(screenX,screenY))
                if board[r][c] == 'Bb':
                        self.screen.blit(self.black_bishop,(screenX,screenY))
                if board[r][c] == 'Bq':
                        self.screen.blit(self.black_queen,(screenX,screenY))
                if board[r][c] == 'Ba':
                        self.screen.blit(self.black_king,(screenX,screenY))
                if board[r][c] == 'Wp':
                        self.screen.blit(self.white_pawn,(screenX,screenY))
                if board[r][c] == 'Wr':
                        self.screen.blit(self.white_rook,(screenX,screenY))
                if board[r][c] == 'Wh':
                        self.screen.blit(self.white_knight,(screenX,screenY))
                if board[r][c] == 'Wb':
                        self.screen.blit(self.white_bishop,(screenX,screenY))
                if board[r][c] == 'Wq':
                        self.screen.blit(self.white_queen,(screenX,screenY))
                if board[r][c] == 'Wa':
                        self.screen.blit(self.white_king,(screenX,screenY))
                
        pygame.display.flip()

    def endGame(self,board):
        self.Draw(board) 
        pygame.event.set_blocked(MOUSEMOTION)
        while True:
            e = pygame.event.wait()
            if e.type is KEYDOWN:
                    pygame.quit()
                    sys.exit(0)
            if e.type is QUIT:
                    pygame.quit()
                    sys.exit(0)

                    
    def getPlayerInput(self,board,currentColor):
        fromSquareChosen = False
        toSquareChosen = False
        while not fromSquareChosen or not toSquareChosen:
            squareClicked = []
            pygame.event.set_blocked(MOUSEMOTION)
            e = pygame.event.wait()
            if e.type is KEYDOWN:
                if e.key is K_ESCAPE:
                    fromSquareChosen = 0
                    fromTuple = []
            if e.type is MOUSEBUTTONDOWN:
                (mouseX,mouseY) = pygame.mouse.get_pos()
                squareClicked = self.convertToChess((mouseX,mouseY))
                if squareClicked[0]<0 or squareClicked[0]>7 or squareClicked[1]<0 or squareClicked[1]>7:
                    squareClicked = [] 
            if e.type is QUIT:
                pygame.quit()
                sys.exit(0)
                            
            
                            
            if not fromSquareChosen and not toSquareChosen:
                self.draw(board)
                if squareClicked != []:
                    (r,c) = squareClicked
                    if currentColor == 'B' and 'B' in board[r][c]:
                        if len(self.Rules.getValidMoves(board,squareClicked))>0:
                            fromSquareChosen = True
                            fromTuple = squareClicked
                    elif currentColor == 'W' and 'W' in board[r][c]:
                        if len(self.Rules.getValidMoves(board,squareClicked))>0:
                            fromSquareChosen = True
                            fromTuple = squareClicked
                                    
            elif fromSquareChosen and not toSquareChosen:
                possibleDestinations = self.Rules.getValidMoves(board,fromTuple)
                self.draw(board,possibleDestinations)
                if squareClicked != []:
                    (r,c) = squareClicked
                    if squareClicked in possibleDestinations:
                        toSquareChosen = True
                        toTuple = squareClicked
                    elif currentColor == 'B' and 'B' in board[r][c]:
                        if squareClicked == fromTuple:
                            fromSquareChosen = False
                        elif len(self.Rules.getValidMoves(board,squareClicked))>0:
                            fromSquareChosen = True
                            fromTuple = squareClicked
                        else:
                            fromSquareChosen = 0 
                    elif currentColor == 'W' and 'W' in board[r][c]:
                        if squareClicked == fromTuple:
                            fromSquareChosen = False
                        elif len(self.Rules.getValidMoves(board,squareClicked))>0:
                            fromSquareChosen = 1
                            fromTuple = squareClicked
                        else:
                            fromSquareChosen = False
                    else: 
                        fromSquareChosen = False

        return (fromTuple,toTuple)

    def endGame(self,board):
        self.Draw(board) 
        pygame.event.set_blocked(MOUSEMOTION)
        while True:
            e = pygame.event.wait()
            if e.type is KEYDOWN:
                    pygame.quit()
                    sys.exit(0)
            if e.type is QUIT:
                    pygame.quit()
                    sys.exit(0)


    

