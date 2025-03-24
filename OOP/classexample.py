class WhiteBoard:
    #Constructor
    def __init__(self,nm,isMag,content):
        self.numberMarkers = nm #Class attribute
        self.isMagnetic = isMag #Class attribute
        self.boardContent = content #Class attribute
    
    #Class Methods
    def addMarker(self,amountofMarkers):
        self.numberMarkers = self.numberMarkers + amountofMarkers
    def writeOnBoard(self,boardStuff):
        self.boardContent = self.boardContent + boardStuff
    def eraseBoard(self):
        self.boardContent = ''
    def printBoard(self):
        print(self.boardContent)

#Let's create our whiteboard
my_board = WhiteBoard(15,True,'')
#Let's add some markers
my_board.addMarker(2)
#Let's see how many markers there are on the board
print(my_board.numberMarkers)
