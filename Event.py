import random

class Event:


    def __init__(self,map,MaxX=6,MaxY=4):
        self.CMap=map
        self.CMaxX=MaxX
        self.CMaxY=MaxY
        self.Cx=-1
        self.Cy=-1
        self.led=2



    def CommonPath(self, val,Cx,Cy):
    #This is going to make (CMaxX) Path ways that will simply attempt to get to the other side.
    #Then this method will record the amount time a pathway is walked giving us a good place for an event.
    #This has an issue with dead ends,there is a case for instance "000011110111110000111111" will give a False negative.
        if (self.CMap[Cy][Cx] == "1"):
            return val
        val[Cy][Cx] = val[Cy][Cx] + 1
        while (Cx < self.CMaxX - 1):
            found = False
            if self.CMap[Cy][Cx + 1] == "0":
                Cx = Cx + 1
                val[Cy][Cx] = val[Cy][Cx] + 1
                found = True
            if Cy + 1 < self.CMaxY and not found:
                if self.CMap[Cy + 1][Cx] == "0":
                    Cy = Cy + 1
                    val[Cy][Cx] = val[Cy][Cx] + 1
                    found = True
            if Cy - 1 > 0 and not found:
                if self.CMap[Cy - 1][Cx] == "0":
                    Cy = Cy - 1
                    val[Cy][Cx] = val[Cy][Cx] + 1
                    found = True
            if not found:
                print("Dead end")
                return val
        print("Path Found")
        return val


    def LargestIntersection(self, val):
    #This simply finds the largest amount of times that a place
        Intersection = 0
        for i in range(0, self.CMaxX):
            for j in range(0, self.CMaxY):
                if val[i][j] > Intersection:
                    Intersection = val[i][j]
        return Intersection


    def CoordinateOfLargestIntersections(self, val, IntersectionValue):
        #Given the map of intersections and the greatest amount of intersections.
        #We simply search through the intersections map to find the coordinates of every instance.

        Coordinates = []
        while(len(Coordinates)<6):
            for i in range(0, self.CMaxX):
                for j in range(0, self.CMaxY):
                    if val[i][j] == IntersectionValue:
                        coord = (i, j);
                        Coordinates.append(coord)
        IntersectionValue=IntersectionValue-1
        return Coordinates

    def SelectCoordinates(self,Coordinates):
        random.shuffle(Coordinates)
        print(Coordinates)
        NCoordinates=[]
        for i in range(0,4):
            NCoordinates.append(Coordinates[i])
        for q in range(4,len(Coordinates)):
            if Coordinates[q][0]==self.CMaxX-1:
                NCoordinates.append(Coordinates[q])
                break

        return NCoordinates
    def AddEvents(self,map):
        for i in range(0,self.CMaxY):
            for j in range(0,self.CMaxX):
                if(self.Cx!=-1 and self.Cy!=-1):
                    map[self.Cy][self.Cy]=self.led
                    break
        return map








class Challenge(Event):

    def __init__(self):
        super.__init__()
        self.led=3

    def FindLocation(self):





    # def main():
    #     CMap = [["0" for i in range(4)] for j in range(4)]
    #     val = [[0 for i in range(4)] for j in range(4)]
    #     CMap[0][3] = "1"
    #     CMap[3][3] = "1"
    #     for q in range(0, len(CMap[0])):
    #         CMap[1][q] = "1"
    #     Cx = 0
    #     Cy = 0
    #     CMaxX = 4
    #     CMaxY = 4
    #     i = 0
    #     for i in range(0, CMaxY):
    #         val = CommonPath(CMap, val, 0, i)
    #     Coordinates=CoordinateOfLargestIntersections(val, LargestIntersection(val))
    #     print(Coordinates)
    #     print(val)