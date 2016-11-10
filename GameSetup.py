#Importing all Tkinter modules
from Tkinter import *

class GameSetup:

        def __init__(self):
		self.root = Tk()
		self.root.title("Welcome to MyChessAI!")
		self.frame = Frame(self.root)
		self.frame.pack()
		
		self.Message = StringVar()
		Label(self.frame, textvariable=self.Message).grid(row=0)
		self.Message.set("Please enter game options.")

		Label(self.frame, text="Name").grid(row=1,column=1)
		Label(self.frame, text="Type").grid(row=1,column=2)
		
		Label(self.frame, text="Player 1 (White)").grid(row=2,column=0)
		self.entry_player1Name = Entry(self.frame)
		self.entry_player1Name.grid(row=2,column=1)
		self.entry_player1Name.insert(ANCHOR,"Your name")
		
		self.tk_player1Type = StringVar()
		Radiobutton(self.frame, text="Human",variable=self.tk_player1Type,value="human").grid(row=2,column=2)
		self.tk_player1Type.set("human")
			
		
		Label(self.frame, text="Player 2 (Black)").grid(row=3,column=0)
		self.entry_player2Name = Entry(self.frame)
		self.entry_player2Name.grid(row=3,column=1)
		self.entry_player2Name.insert(ANCHOR,"Kasparov")
		
		self.tk_player2Type = StringVar()
		Radiobutton(self.frame, text="Human",variable=self.tk_player2Type,value="human").grid(row=3,column=2)
		Radiobutton(self.frame, text="Random AI",variable=self.tk_player2Type,value="randomAI").grid(row=3,column=3)
		Radiobutton(self.frame, text="Minmax AI",variable=self.tk_player2Type,value="minmaxAI").grid(row=3,column=4)
		self.tk_player2Type.set("minmaxAI")
		

		b = Button(self.frame, text="Start the Game!", command=self.ok)
		b.grid(row=4,column=1)

	def ok(self):
		self.player1Name = self.entry_player1Name.get()
		#hardcoded so that player 1 is always white
		self.player1Colour = "white"
		self.player1Type = self.tk_player1Type.get()
		self.player2Name = self.entry_player2Name.get()
		self.player2Colour = "black"
		self.player2Type = self.tk_player2Type.get()
		
		if self.player1Name != "" and self.player2Name != "":
			self.frame.destroy()
		else:
			if self.player1Name == "":
				self.entry_player1Name.insert(ANCHOR,"Kasparov")
			if self.player2Name == "":
				self.entry_player2Name.insert(ANCHOR,"Abhay")

	def getGameInfo(self):
		self.root.wait_window(self.frame) #waits for frame to be destroyed
		self.root.destroy()
		return (self.player1Name, self.player1Colour, self.player1Type, 
				self.player2Name, self.player2Colour, self.player2Type)



