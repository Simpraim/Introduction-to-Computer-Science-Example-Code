<<<<<<< HEAD
print(hello)
=======
class WhiteBoard:
    #Constructor
    def __init__(self,nm,isMag,content):
        self.numberMarkers = nm #Class attribute
        self.isMagnetic = isMag #Class attribute
        self.boardContent = content #Class attribute
    
    #Class Methods
    def addMarker(self,amountofMarkers):
        self.numberMarkers = self.numberMarkers + amountofMarkers
    def removeMarker(self, amountofMarkers):
        self.numberMarkers = self.numberMarkers - amountofMarkers
    def writeOnBoard(self,boardStuff):
        self.boardContent = self.boardContent + boardStuff
    def eraseBoard(self):
        self.boardContent = ''
    def printBoard(self):
        print(self.boardContent)
    def printObject(self):
        print(f'The board has {self.numberMarkers} markers \n The value for if it is magnetic is {self.isMagnetic}\n Here is the content on the board {self.boardContent}')

#Let's create our whiteboard
bc = 'hi'
my_board = WhiteBoard(15,True,bc)
#Let's add some markers
my_board.addMarker(2)
#Let's see how many markers there are on the board

my_board.writeOnBoard('Stephen')
my_board.printBoard()
my_board.eraseBoard()
my_board.printBoard()
my_board.removeMarker(my_board.numberMarkers)

>>>>>>> 4ca46d12b8fe69e836be931704515a085a19ea69
