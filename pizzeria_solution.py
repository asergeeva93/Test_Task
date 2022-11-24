import numpy as np
from Pizzeria import Pizzeria
from Zcity import Zcity

def main():
    raw_data = readInput()
    if raw_data == False:
        return
    else:
        z_city = Zcity(int(raw_data[0][0]), int(raw_data[0][0]))
        findMax(raw_data, z_city)

def readInput():
    raw_input = []
    while True:
      try:
          line = input()
      except EOFError:
          break
      data = line.split()
      for i in data:
          try:
              int(i)
          except ValueError:
              print("Only integers are accepted as input. Please restart the programme and try again")
              return False
      raw_input.append(data)
      if len(raw_input) == int(raw_input[0][1])+1:
          return raw_input

def createPizzeria(raw_data, z_city):
    for i in range(1,len(raw_data)):
        pizzeria = Pizzeria(int(raw_data[i][2]), int(raw_data[i][0]), int(raw_data[i][1]))
        coords = pizzeria.findRadius(z_city.getN())
        z_city.moveIn(coords)

def findMax(raw_data, z_city):
    createPizzeria(raw_data, z_city)
    max_value = int(np.max(z_city.getZCity()))
    print(max_value)
    return(max_value)


if __name__ == "__main__":
    main()
