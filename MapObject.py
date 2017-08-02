import random
import Databas as DB
import os.path


class Map:
    def __init__(self):
        size=int(input("Please enter the size of the map (ex. 3= 3x3)"))
        self.size=size
        self.size2=size*size

        self.map = [[0] * self.size for i in range(self.size)]

        for i in range(0,self.size):
            for j in range(0,self.size):
                self.map[i][j]=str(i)+str(j)


    def AddToMap(self,ReversedBinary):
        #this function requires that the integer value must be reversed so that it is more convienent to enter into the map varaible.
        for i in range(0, self.size):
            for j in range(0, self.size):
                singleChar = ReversedBinary[-1:]
                ReversedBinary = ReversedBinary[:-1]
                self.map[i][j] = singleChar
        return self.map

    def Display(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                print(self.map[i][j], end=" ")
            print()

    def DecToFormatVal(self,val):
        #formating will tend to the needs of the size so for 3x3 there will be 9 digits and 5x5 25 digits.

        form="{0:0%db}"%(self.size2)
        sNum = form.format(val)
        #print(sNum)
        # reverse the value so it is easier to enter into the array
        sNum = sNum[::-1]

        #print(sNum)
        return sNum

    def MaxBinVal(self):
        #this will add 1's to every possible position of the string giving us the maximum combinations
        sVal=str(1)*self.size2
        return int(sVal, 2)

    def PFinder(self,x=0,y=0,i=0,found=True):
        # So there is an issue where if it finds a spot but the spot doesnt go anywhere,
        # the function will return the wrong value.
        if(x<0 or y<0 or x>=self.size or y>=self.size):
            #to catch if x and y values will go out of bounds
            return 0
        if(i>self.size2):
            #if the value exceeds the amount of blocks in the map
            return 0

        if((x==0 or x==self.size-1 or y==0 or y==self.size-1)and self.map[y][x]=="0"):
            #if there is a tile on the first or last column or the first or last row then there is an entrance.
            self.map[y][x]=self.map[y][x]+"f"
            return 1 + self.PFinder(x,y-1,i+1,False)+self.PFinder(x+1,y,i+1,False)+self.PFinder(x,y+1,i+1,False)+self.PFinder(x-1,y,i+1,False)
        # This is the recusive statement if the function returns a number that is greater than 2 then it is an acceptable map
        #the functions will look in all of the cardinal directionals to determine if there is a path.
        if(self.map[y][x]=="0"):
            return 0+self.PFinder(x,y-1,i+1,False)+self.PFinder(x+1,y,i+1,False)+self.PFinder(x,y+1,i+1,False)+self.PFinder(x-1,y,i+1,False)



        if (self.map[y][x] == "1" and found and i<self.size2-1):
            # handles if the function starts on a wall
            # adding the f to the statement colors the value so there are no continous recursions
            self.map[y][x] = self.map[y][x] + "f"
            if (x == 2):  # 4 for 5x5
                # this will prevent the function from going out of bounds
                x = 0
                return 0 + self.PFinder(x, y + 1, i + 1)
            else:
                return 0 + self.PFinder(x + 1, y, i + 1)
        else:
            return 0

    def CreateDB(self):
        # if(os.path.isfile("Maps.db")):
        #     print("File is already create are you sure you want to do this (Y/N)")
        #     user=input().capitalize()
        #     if(user=="N"):
        #         print("Creating Database is cancelled.")
        #         return

        print("Creating Database")
        DB.create_table()

        for i in range(self.MaxBinVal()):
            sNum = self.DecToFormatVal(i)
            self.AddToMap(sNum)
            if (self.PFinder() > 1):
                DB.data_entry(i, sNum)
                # print("Added "+str(i)+"to the data base")


        print("DataBase Complete")

    def RandMap(self,size=3):
        #if(os.path.isfile("Maps.db")):
            randMap = random.randint(0, DB.rowCount())
            sNum = self.DecToFormatVal(randMap)
            self.AddToMap(sNum)
            self.Display()
            return

        #print("Database is not created please enter 1 to create one")
        #return
    # def test(self):
    #     self.MaxBinVal()


