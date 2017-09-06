import random
import Databas as DB
import timeit
#import Ra as RC
# import os.path

class Map:
    def __init__(self,xsize=6,ysize=4):

        self.xsize=xsize
        self.ysize=ysize
        self.area=xsize*ysize
        self.MapGraph={}

        self.map = [[0] * self.xsize for i in range(self.ysize)]

        for i in range(0,self.ysize):
            for j in range(0,self.xsize):
                #print("i="+str(i)+"j="+str(j))
                self.map[i][j]="i="+str(i)+"j="+str(j)
                #print()

    def AddCurrentVal(self,val):
        self.CurrentVal=val

    def AddToMap(self,ReversedBinary):
        #this function requires that the integer value must be reversed so that it is more convienent to enter into the map varaible.
        for i in range(0, self.ysize):
            for j in range(0, self.xsize):
                singleChar = ReversedBinary[-1:]
                ReversedBinary = ReversedBinary[:-1]
                self.map[i][j] = singleChar
        #self.ToGraph()
        #print(self.MapGraph)
        return self.map

    def bfs_paths(self,graph, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def Clear(self):
        RBin=self.GetCurrentVal()
        self.AddToMap(RBin)

    def CreateDB(self):
        # if(os.path.isfile("Maps.db")):
        #     print("File is already create are you sure you want to do this (Y/N)")
        #     user=input().capitalize()
        #     if(user=="N"):
        #         print("Creating Database is cancelled.")
        #         return
        start = timeit.timeit()
        print("Creating Database")
        DB.create_table()

        for i in range(self.MaxBinVal()):
            sNum = self.DecToFormatVal(i)
            self.AddCurrentVal(sNum)
            self.AddToMap(sNum)
            self.ToGraph()
            PathLength=0
            #print("path to the start and goal of program")
            mapstart=timeit.timeit()
            print("Working on map "+str(i))
            for q in range(0,3):
                for j in range(0,5):
                    goal=str(q)+str(j)
                    listPath=list(self.bfs_paths(self.MapGraph, '00', goal))
                    PathofCurrentList=self.findLongestPath(listPath)
                    #print(PathofCurrentList)
                    if(PathofCurrentList>PathLength):
                        PathLength=PathofCurrentList
                print(PathLength)
                if (PathLength > 6):
                    print(i, " has PASSED with a length of " , PathLength)
                    DB.data_entry(j, sNum)
                     #print("Added "+str(i)+"to the data base")
               # else:
               #     print(i, " has FAILED")
                mapend = timeit.timeit()
                maptime = mapend - mapstart
                print( "Time to complete map "+str(i)+" : "+str(maptime))

        print("DataBase Complete")
        end = timeit.timeit()
        print("Total Time taken:")
        print(end - start)

    def DecToFormatVal(self, val):
        # formating will tend to the needs of the size so for 3x3 there will be 9 digits and 5x5 25 digits.

        form = "{0:0%db}" % (self.area)
        sNum = form.format(val)
        # print(sNum)
        # reverse the value so it is easier to enter into the array
        sNum = sNum[::-1]

        # print(sNum)
        return sNum

    def Display(self):
        for i in range(0,self.ysize):
            for j in range(0,self.xsize):
                print(self.map[i][j], end=" ")
            print()

    def GetCurrentVal(self):
        return self.CurrentVal

    def findLongestPath(self, ListPath):
        longestPath = 0
        for i in range(0, len(ListPath)):
            if (len(ListPath[i]) > longestPath):
                longestPath = len(ListPath[i])
        return longestPath

    def MaxBinVal(self):
        #this will add 1's to every possible position of the string giving us the maximum combinations
        sVal=str(1)*self.area
        return int(sVal, 2)

    def ToGraph(self):
        global AlphaTrack
        AlphaTrack=0
        for i in range(0,self.ysize):
            for j in range(0,self.xsize):
                singleEdge=""
                edges = []
                Current=str(i)+str(j)


                #north Edge
                if not (i-1<0):
                    if self.map[i-1][j]=="0":
                        singleEdge=str(i-1)+str(j)
                        edges.insert(-1,singleEdge)
                #East Edge
                if not (j+1>=self.xsize):
                    if self.map[i][j+1]=="0":
                        singleEdge=str(i)+str(j+1)
                        edges.insert(-1,singleEdge)
                #South Edge
                if not (i+1>=self.ysize):
                    if self.map[i+1][j]=="0":
                        singleEdge=str(i+1)+str(j)
                        edges.insert(-1,singleEdge)
                #West Edge
                if not (j-1<0):
                    if self.map[i][j-1]=="0":
                        singleEdge=str(i)+str(j-1)
                        edges.insert(-1,singleEdge)
                self.MapGraph[Current]=set(edges)

    def RandMap(self,size=3):
        #if(os.path.isfile("Maps.db")):
            randMap = random.randint(0, DB.rowCount())

            sNum = self.DecToFormatVal(randMap)

            print("Selected val", randMap,"out of the possible ", DB.rowCount(),"with the code of ",sNum)
            self.AddToMap(sNum)
            self.Display()
            return

        #print("Database is not created please enter 1 to create one")
        #return

    def test(self):
        self.MaxBinVal()

    #def MapDemo(self):
     #   Demo1=ServoControl(11)
     #   Demo2=ServoControl(13)
     #   Demo3=ServoControl(15)