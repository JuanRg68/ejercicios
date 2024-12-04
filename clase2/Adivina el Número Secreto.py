ns = 7
intento = int(input(" Trata de adivinar el número secreto (del 1 al 10.) "))

while intento != ns:
    if intento < ns:
        print (" El número es mayor. ")
    else:
        print (" El número es menor. ")
    intento = int(input(" Intenta de núevo: "))


print(" El número que escogiste, es el correcto. Felicidades! ")
