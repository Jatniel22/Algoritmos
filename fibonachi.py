""""La secuencia de Fibonacci es una secuencia matemática en la cual cada número es la suma de los dos números anteriores. La secuencia comienza generalmente con 0 y 1, y a partir de ahí se genera la siguiente serie de números: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, y así sucesivamente.

La fórmula matemática para calcular los términos de la secuencia de Fibonacci es la siguiente:

Fn = Fn-1 + Fn-2"""
import tkinter as vent

def fibonachi(num):
    fibonachi.cont += 1
    if(num<=1):
        return 1
    else:

        return fibonachi(num-1) + fibonachi(num-2)
    
    
fibonachi.cont=0
n=int(input("digite un numero:"))
num=n-1
print("la secuencia es: ",fibonachi(num))
print("fibonachi se ejecuta {}".format(fibonachi.cont))