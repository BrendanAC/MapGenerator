import random
class Map:
    def __init__(self, x=0,y=0):
        mapAccpetable=False

        self.map = [[0] * x for i in range(y)]
        for i in range(0,x):
            for j in range(0,y):
                self.map[i][j]="0"

    def New(self,x,y):

        for i in range(0,x):
            for j in range(0,y):

                self.map[i][j]=random.randint(0,1)