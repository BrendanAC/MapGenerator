import random
import Databas

class Map:
    def __init__(self, x=0,y=0):
        mapAccpetable=False
        self.x=x
        self.y=y

        self.map = [[0] * x for i in range(y)]
        for i in range(0,x):
            for j in range(0,y):
                self.map[i][j]=str(i)+str(j)


    def AddToMap(self,ReversedBinary,size=5):
        #this function requires that the integer value must be reversed so that it is more convienent to enter into the map varaible.
        for i in range(0, size):
            for j in range(0, size):
                singleChar = ReversedBinary[-1:]
                ReversedBinary = ReversedBinary[:-1]
                self.map[i][j] = singleChar
        return self.map

    def Display(self,size=5):
        for i in range(0, size):
            for j in range(0, size):
                print(self.map[i][j], end=" ")
            print()

    def DecToFormatVal(self,val):
        # makes the value 25 char long

        #sNum = "{0:025b}".format(val)
        sNum = "{0:09b}".format(val)
        #print(sNum)


        # reverse the value so it is easier to enter into the array
        sNum = sNum[::-1]

        #print(sNum)
        return sNum

    def PFinder(self,x=0,y=0,i=0):
        if(x<0 or y<0 or x>=3 or y>=3):
            #to catch if x and y values will go out of bounds
            return 0
        if(i>9):
            #if the value exceeds the amount of blocks in the map
            return 0
        if(self.map[y][x]=="1" ):
            #handles if the function starts on a wall
            if(i+1<9):
                #adding the f to the statement colors the value so there are no continous recursions
                self.map[y][x] = self.map[y][x] + "f"
                if(x==2):#4 for 5x5
                    #this will prevent the function from going out of bounds
                    x=0
                    return 0+self.PFinder(x,y+1,i+1)
                else:
                    return 0+self.PFinder(x+1,y,i+1)
        if((x==0 or x==2 or y==0 or y==2)and self.map[y][x]=="0"):
            #if there is a tile on the first or last column or the first or last row then there is an entrance.
            self.map[y][x]=self.map[y][x]+"f"
            return 1 + self.PFinder(x,y-1,i+1)+self.PFinder(x+1,y,i+1)+self.PFinder(x,y+1,i+1)+self.PFinder(x-1,y,i+1)
        # This is the recusive statement if the function returns a number that is greater than 2 then it is an acceptable map
        #the functions will look in all of the cardinal directionals to determine if there is a path.
        if(self.map[y][x]=="0"):
            return 0+self.PFinder(x,y-1,i+1)+self.PFinder(x+1,y,i+1)+self.PFinder(x,y+1,i+1)+self.PFinder(x-1,y,i+1)

        else:
            return 0


