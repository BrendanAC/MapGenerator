from MapObject import Map
from Event import Event
import sys

def Menu():
    print("Enter 1 to create a Database (is required on intial load)")
    print("Enter 2 to generate a new Map")
    print("Enter 3 to Demo map")
    print("Enter 0 to exit program")

def gateKeeper(InitMap,user):
    if(user==str(0)):
        sys.exit()
    if (user==str(1)):
        InitMap.CreateDB()
        return
    if(user==str(2)):
        InitMap.RandMap()
        DMap=Event(InitMap.map)
        Coordinates=DMap.SelectCoordinates()
        DMap.PopulateMap(Coordinates)
        return
    if(user==str(3)):
        InitMap.test()
        return
    else:
        print("Invalid input please try again.")
        return

def main():
    print("Welcome to Map Generator v 1.0")
    InitMap=Map()
    user=-1
    while(user!=0):
        Menu()
        user=input()
        gateKeeper(InitMap,user)

if __name__ == "__main__":
    main()