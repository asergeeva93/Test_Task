import numpy as np

class Zcity:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.z_city = np.zeros(shape=(self.n,self.m))

    def getN(self):
        return self.n

    def getM(self):
        return self.m

    def getZCity(self):
        return self.z_city

    #a fucntion to plot all of the coordinates (excluding ones that are not in te city)
    def moveIn(self, list):
        for i in range (len(list)):
            coord1 = list[i][0]
            coord2 = list[i][1]
            if 1<= coord1 <= self.n and 1<= coord2 <= self.n:
                try:
                    self.z_city[coord1-1][coord2-1] = self.z_city[coord1-1][coord2-1] + 1
                except IndexError:
                    continue
            else:
                continue
