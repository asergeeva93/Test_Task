import numpy as np

class Pizzeria:
    def __init__(self, moves, x, y):
        self.moves = moves
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getMoves(self):
        return self.moves

    #a function that finds the radius(in a shape of a rhombus)of a pizzeria based on its location
    def findRadius(self, size):
        blocks = list()
        blocks.append([self.x,self.y])
        gradient = 1
        if self.x == size:
            UpperBlock = [self.x, self.y]
        else:
            UpperBlock = [self.x+self.moves, self.y]
            for i in range (self.moves-1):
                for i in range(0,gradient):
                    coord1 = [UpperBlock[0]-gradient, UpperBlock[1]-gradient+i]
                    coord2 = [UpperBlock[0]-gradient, UpperBlock[1]+gradient-i]
                    blocks.append(coord1)
                    blocks.append(coord2)
                gradient = gradient + 1
        if self.x == 1:
            LowerBlock = [self.x, self.y]
        else:
            LowerBlock = [self.x-self.moves, self.y]
            gradient = 1
            for i in range (self.moves - 1):
                for i in range(0,gradient):
                    coord1 = [LowerBlock[0]+gradient, LowerBlock[1]-gradient+i]
                    coord2 = [LowerBlock[0]+gradient, LowerBlock[1]+gradient-i]
                    blocks.append(coord1)
                    blocks.append(coord2)
                gradient = gradient + 1
        for i in range (1,self.moves+1):
            coord1 = [self.x-i,self.y]
            coord2 = [self.x+i,self.y]
            coord3 = [self.x,self.y+i]
            coord4 = [self.x,self.y-i]
            blocks.append(coord1)
            blocks.append(coord2)
            blocks.append(coord3)
            blocks.append(coord4)
        return blocks
