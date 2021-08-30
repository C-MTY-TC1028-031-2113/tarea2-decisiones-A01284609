def main():

    grados = int(input("Introduce los grados: "))
    
    if grados < 0 or grados > 360:
        print ("excede")

    else:
        if grados > 0 and grados < 90:
            print ("Cuadrante 1")
        elif grados == 90: 
            print ("eje")
        elif grados > 90 and grados < 180:
            print ("Cuadrante 2")
        elif grados == 180: 
            print ("eje")
        elif grados > 180 and grados < 270:
            print ("Cuadrante 3")
        elif grados == 270: 
            print ("eje")
        elif grados > 270 and grados < 360:
            print ("Cuadrante 4")
        elif grados == 360: 
            print ("eje")

if __name__ == '__main__':
    main()
