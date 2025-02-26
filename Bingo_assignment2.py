
#BINGO CHALLENGE-assignment 2
#looking for the last board to win


#### observer / subscriber approach
class Board:
    def __init__(self,content=[]):
        self.content=content
        self.marked=[False] * len(content)
        self.score=0
        self.hasWon=False

    def mark(self,drawnValue):
        #if value exxist in board mark it as true 
        
        if drawnValue in self.content:
            self.marked[self.content.index(drawnValue)]=True
            self.checkMarked()
        return self.hasWon

    def checkMarked(self):
        boardLen=25
        size=5
        #check rows
        i=0
        while (i<boardLen):
            if not(False in self.marked[i:i+size]):
                self.hasWon=True
                print('BINGOOOOOO!!')
                return
            i+=size
        #check columns
        i=0
        while(i<size):

            if not(False in self.marked[i::size]):
                self.hasWon=True
                print('BINGOOOOOO!!')
                return
            i+=1

    def getUnmarkedSum(self):
        sum=0
        for val, flag in zip(self.content,self.marked):
            if not flag :
                sum=sum+val
        return sum



#####Publisher
class Bingo:
    def __init__(self,):
        self.drawnSet = []
        self.boards = []
        self.winner=0
        self.winnerScore=0

    def addBoard(self,board:Board):
        self.boards.append(board)

    def startdraw(self):

        print('Bingo Night Starts ...')
        lastWinner=Board()
        lastWinDrawnNumber=-1
        winnerNum=-1
        for x in self.drawnSet:
            print('We have drawn number : ',x)
            i=0
            for b in self.boards:
                #if board already marked as winner we continue no need to try to mark it
                if b.hasWon:
                    i+=1
                    continue
                #b.mark() returns if the board won or not
                if b.mark(x):
                    lastWinner=b
                    lastWinDrawnNumber=x
                    winnerNum= i+1
                    print(f'Winner : Board number {winnerNum}')
                    print(f'Score : {b.getUnmarkedSum()*x}')
                i+=1
        print('All Numbers have been drawn')
        if winnerNum!=-1:
            print(f'Last Winner : Board number {winnerNum}')
            print(f'Last Winner Score : {lastWinner.getUnmarkedSum()*lastWinDrawnNumber}')
        else:
            print(f'Bad Luck ... No winners')
            
    def readingInput(self,filePath):
        with open(filePath,"r") as f:
            #reading the first line then converting strings to integers using map()
            self.drawnSet= list(map(int,f.readline().split(',')))
            
            #we read the rest of the input text containing the boards and their values trimmed from empty spaces 
            boardsContent=f.read().strip() 
        # file is closed
        boardsList=boardsContent.split('\n\n') # list containing every board but still in string format 

        for b in boardsList:
            isBlank =True
            tempBoard=[]
            #reading char by char and parsing it into a list of integers
            for c in b :
                if not c.isdigit():
                    if(isBlank==False):
                        tempBoard.append(x)
                    isBlank=True
                    continue
                if(isBlank==True):
                    x=int(c)
                else: 
                    #handling multi digits strings
                    x=x*10+int(c)
                isBlank=False
            tempBoard.append(x)
            self.addBoard(Board(tempBoard))

if __name__ == "__main__":

    path="input.txt"
    short_test_path="test.txt" # input with only 3 tables and first table is guaranteed to win first while second table wins last  

    bingo1=Bingo()   

    #bingo1.readingInput(short_test_path)
    bingo1.readingInput(path)

    #testing input reading/loading 
    #printing the 4th table and the drawnset
    print(f'the drawn set : {bingo1.drawnSet}')
    print(f'board number 1 : {bingo1.boards[0].content}')

    #test  
    bingo1.startdraw() #expected result Last winner is board 22 with score 36975