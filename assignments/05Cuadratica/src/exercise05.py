import math

def main():

    a = int(input("Da el valor de a: "))
    b = int(input("Da el valor de b: "))
    c = int(input("Da el valor de c: "))

    if a == 0 and b == 0:
        print ("No tiene solucion")

    elif a == 0 and b != 0:
        print (-c / b)

    elif a != 0 and b != 0:
        if (b**2 -4*a*c) < 0:
            print ("Raices complejas")

        elif (b**2 - 4*a*c) > 0:
            x1 = (-b + math.sqrt(b**2 -4*a*c)) / (2*a)
            x2 = (-b - math.sqrt(b**2 -4*a*c)) / (2*a)
            print (x1)
            print (x2)

        else:
            print ((-b / (2*a)))


if __name__ == '__main__':
    main()
