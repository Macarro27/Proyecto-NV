def taza():
    print("Desea una taza:\n"
          "A - Pequeña\n"
          "B - Mediana\n"
          "C - Grande\n")
    opcion=input("Ingrese su respuesta: ")
    if opcion=="A" or opcion=="a":
        print("Preparando taza pequeña...")
    elif opcion=="B" or opcion=="b":
        print("Preparando taza mediana...")
    elif opcion=="C" or opcion=="c":
        print("Preparando taza grande...")
    else:
        print("Opcion no valida")

def cafeina():
    print("Desea cafeina:\n"
          "A - Baja\n"
          "B - Media\n"
          "C - Alta\n")
    opcion = input("Ingrese su respuesta: ")
    if opcion == "A" or opcion=="a":
        print("Preparando cafeina baja...")
    elif opcion == "B" or opcion=="b":
        print("Preparando cafeina media...")
    elif opcion == "C" or opcion=="c":
        print("Preparando cafeina alta...")
    else:
        print("Opcion no valida")

def leche_y_Espuma():
    opcion=input("¿Desea que su café tenga leche? (S/N): ")
    if opcion=="S" or opcion=="s":
        print("Agregando leche...")
        opcion=input("¿Desea que su café tenga espuma? (S/N): ")
        if opcion=="S" or opcion=="s":
            print("Agregando espuma...")
        else:
            print("Cancelando opcion...")
    elif opcion=="N" or opcion=="n":
        opcion=input("¿Desea que su café tenga espuma? (S/N): ")
        if opcion == "S" or opcion=="s":
            print("Agregando espuma...")
        else:
            print("Cancelando opcion...")
    else:
        print("Opcion no valida")

print("Bienvenido Usuario")
inicio=input("¿Desea preparar una taza de café ahora? (S/N): ")

while inicio=="S" or inicio=="s":
    print("Menu")
    opcion=input("A - Tamaño de la taza\n"
          "B - Intensidad de la cafeina\n"
          "C - Leche y Espuma\n"
          "D - Salir del menu\n")
    if opcion=="A" or opcion=="a":
        taza()
    elif opcion=="B" or opcion=="b":
        cafeina()
    elif opcion=="C" or opcion=="c":
        leche_y_Espuma()
    elif opcion=="D" or opcion=="d":
        print("Saliendo del menu")
        inicio="N"
        print("Su café esta listo...")
    else:
        print("Opcion no valida")

