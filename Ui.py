from MapObject import Map
import sys

def Menu():
    print("Enter 1 to create a Database (is required on intial load)")
    print("Enter 2 to generate a new Map")
    print("Enter 3 to Demo map")
    print("Enter 0 to exit program")

def gateKeeper(Localmap,user):
    if(user==str(0)):
        sys.exit()
    if (user==str(1)):
        Localmap.CreateDB()
        return
    if(user==str(2)):
        Localmap.RandMap()
        return
    if(user==str(3)):
        Localmap.test()
        return
    else:
        print("Invalid input please try again.")
        return

def main():
    print("Welcome to Map Generator v 1.0")
    Localmap=Map()
    user=-1
    while(user!=0):
        Menu()
        user=input()
        gateKeeper(Localmap,user)

if __name__ == "__main__":
    main()