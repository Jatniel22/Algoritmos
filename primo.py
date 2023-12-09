cont=0
x=int(input("digite el numero: "))
for i in range(1, x+1):
    if(x%i==0):
        cont+=1

if(cont<3):
    print("el numero {} es primo".format(x))
else:
    for i in range(1, x+1):
        if(x%i==0):
            print(i)
            