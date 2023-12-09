import time
import numpy as np
import matplotlib.pyplot as plt

TAMANO =8
numsol =0
tablero = np.zeros((TAMANO,TAMANO), dtype=np.int32)
tiempo=time.time()

def buscarCaballo (cual):
    for fila in range(TAMANO):
        for col in range(TAMANO):
            if tablero[fila, col] == cual: return fila,col

def pintarTableroGraf ():
    for x in range(TAMANO+1):
        plt.plot ([0,TAMANO],[x,x], color="gray")
        plt.plot ([x,x],[0,TAMANO], color="gray")
    X=[]
    Y=[]
    for x in range(1, TAMANO*TAMANO + 1):
        fila,col = buscarCaballo(x)
        X.append([col + 0.5])
        Y.append([TAMANO - fila - 0.5])
        plt.text(col+0.5, TAMANO - fila - 0.5, str(x))
    plt.plot(X,Y)
    plt.suptitle("Knight's tour",fontsize=16)
    plt.show()

def Resolver (row, col, counter):
    global TAMANO
    global numsol
    for i in [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]:
        new_x = row + i[0]
        new_y = col + i[1]
        if new_x < TAMANO and new_x >= 0 and new_y < TAMANO and new_y >= 0 and tablero[new_x,new_y] == 0:
            tablero[new_x,new_y] = counter
            if counter >= TAMANO * TAMANO:
                numsol += 1
                print("··································································")
                print("#", numsol, ", tiempo:", time.time() - tiempo)
                print(tablero)
                pintarTableroGraf()
            else:
                Resolver (new_x, new_y, counter + 1)
            tablero[new_x, new_y] = 0

tablero[3, 2] = 1
Resolver(3, 2, 2)