from MapObject import Map
def main():
    print("Welcome to Map Generator v 1.0")
    x=10
    y=10
    Localmap=Map(x,y)
    Localmap=Map.New(x, y)
    print(Localmap)

if __name__ == "__main__":
    main()