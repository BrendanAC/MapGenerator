from MapObject import Map
def main():
    print("Welcome to Map Generator v 1.0")
    x=5
    y=5
    Localmap=Map(x, y)
    Localmap.New()

    for i in range(0, x):
        for j in range(0, y):
            print(Localmap.map[i][j],end=" ")
        print()

if __name__ == "__main__":
    main()