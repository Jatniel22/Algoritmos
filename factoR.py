def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("\t\t\t_____________________________________")
n=int(input("\t\t\t|digite el numero: "))

print("\t\t\t el factorial es: ",factorial(n))