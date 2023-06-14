#Ejercicio 1
"""Imprimir los primeros 20 números naturales."""
def ej1():
    for i in range(1,21):
        print(i)

def ej2(numero):
    for i in range(0,11):
        print(i*numero)

def ej3():
    flag = True
    while flag:
        x = int(input("Ingrese el número menor: "))
        y = int(input("Ingrese el número mayor: "))
        if x <= y:
            flag = False
        else:
            print("Ingrese un número menor que el otro.")
    for i in range(x,y+1):
        print(i)

def ej4():
    """Dada la siguiente secuencia de números:
numeros = [12 , 75 , 150 , 180 , 145 , 525 , 50]
imprimir los números divisibles por 5 menores a 150"""
    numeros = [12, 75, 150, 180, 145, 525, 50]
    for i in numeros:
        if i % 5 == 0 and i < 150:
            print(i)

def ej5():
    """Imprimir los primeros 10 valores de la secuencia de Fibonacci. La secuencia de Fibonacci es una serie
de números en la cual los dos primeros números son 0 y 1, y el siguiente número se corresponde a la
suma de los dos números anteriores. Resultado esperado:
0 1 1 2 3 5 8 13 21 34
"""
    x = 0
    print (x)
    y = 1
    print(y)
    for i in range(0,8):
        mostrar = x + y
        print(mostrar)
        if i % 2 == 0:
            x = mostrar
        else:
            y = mostrar

def ej6():
    """Imprimir el valor factorial del número 5 usando un bucle. El valor factorial (símbolo: !) se obtiene de
multiplicar todos los números enteros desde el número elegido hasta 1. Resultado esperado: 120
"""
    numero = 5
    for i in range(1,numero):
        numero *= i
    print(numero)

def ej8():
    """Resuelva los siguientes ejercicios
a. Calcular el cuadrado de los primeros 10 números enteros.
b. Calcular la suma de los números enteros entre 0 y 100 inclusive.
c. Calcular la suma de los números pares menores a 100. ¿Cuántos números pares hay menores a
100?
d. Calcular la suma de los números impares menores a 100. ¿Cuántos números impares hay menores
a 100?"""
    #ejercicio a
    lista = []
    for i in range (1,11):
        lista.append(i**2)
    print(lista,sep = ",")
    #ejercicio b
    x = 0
    for i in range (1,101):
        x += i
    print(x)
    #ejercicio c
    x = 0
    count = 1
    for i in range(1,100):
        if i % 2 == 0:
            x += i
            count += 1
    print("El total es",x,"Hay",count,"números pares")
    #ejercicio d
    x = 0
    count = 0
    for i in range(1,100):
        if i % 2 != 0:
            x += i
            count += 1
    print("El total es",x,"Hay",count,"números impares")    
    
def ej10():
    """Escriba un programa que dada una secuencia de números y un valor de umbral vaya sumando los
números de la secuencia hasta que la suma alcance el umbral. Utilice break para terminar la ejecución
del bucle cuando la suma alcance el umbral.
Resultados esperados:
Práctica 4 2022 Página 1/2
umbral = 21
valores = [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]
# suma -> 21
umbral = 34
valores = [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]
# suma -> 34
umbral = 100
valores = [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]
# suma -> 43
    """
    umbral = 40
    suma = 0
    valores = [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]
    for i in valores:
        if suma+i <= umbral:
            suma += i
        else:
            break
    print(suma)

def ej11():
    """Escriba un programa que dada una secuencia numérica compute la suma de los números pares. Utilice
un bucle while y la sentencia continue para saltear los casos donde el número no sea par.
Resultados esperados:
valores = [1 , 2 , 3 , 4 , 5 , 6 , 7, 8 , 9 , 10]
# suma -> 30
valores = [1 , 4 , 7 , 10]
# suma -> 14
"""
    valores = [1 , 4 , 7 , 10]
    i = 0
    suma = 0
    while i < len(valores):
        if valores[i]%2 != 0:
            i += 1
            continue
        suma += valores[i]
        i += 1
    print(suma)

def ej12():
    """Escriba un programa que solicite un numero entero al usuario y compute la suma de todos los numeros
naturales menores a él. Este programa debe ser interactivo. Es decir, el programa solicita un numero al
usuario, devuelve la suma, y solicita un nuevo número. Esto continúa así hasta que el usuario ingresa
"salir", determinando que el programa debe terminar. Utilice un bucle while para resolver este
problema. Tenga en cuenta la sentencia break para determinar la interrupción del bucle. Ejemplos:"""
    flag = 1
    while flag:
        numero = int(input("Ingrese un numero:"))
        for i in range(numero-1,0,-1):
            numero += i 
        print(numero)

        flag = int(input("¿Desea intentar con otro número? 1- Si, 0-No")) 

def ej13():
    """Una mañana ponés un billete en la vereda al lado del Monumento a la Bandera. A partir de ahí, cada
día vas y duplicás la cantidad de billetes, apilándolos prolijamente. ¿Cuánto tiempo pasa antes de que
la pila de billetes sea más alta que la del Monumento? Considere los siguientes valores para comenzar
a resolver el problema:
billete_grosor = 0.11 * 0.001 # grosor de un billete en metros
altura_monumento = 70 # altura en metros
billetes_n = 1
dia = 1
Utilice un bucle while para resolver el problema"""
    billete_grosor = 0.11 * 0.001 # grosor de un billete en metros
    altura_monumento = 70 # altura en metros
    billetes_n = 1
    dia = 1
    altura_billetes = billete_grosor * billetes_n
    while altura_billetes<= altura_monumento:
        billetes_n *= 2
        dia += 1
        altura_billetes = billete_grosor * billetes_n
    print("Con",billetes_n,"billetes y",dia,"días, se superó la altura del monumento.")

def ej14():
    """Escriba un programa reciba dos números como parámetros, y compute cuántos múltiplos del primero
hay, que sean menores que el segundo.
a. Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
b. Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor
que el segundo.
c. Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?"""
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    cantidad_multiplos = 0
    for i in range(0,n2):
        if i*n1 <= n2:
            cantidad_multiplos += 1
        else:
            break
    print(cantidad_multiplos)


def main():
    flag = 1
    print("Ejercicio 1")
    print("Ejercicio 2")
    print("Ejercicio 3")
    print("Ejercicio 4")
    print("Ejercicio 5")
    print("Ejercicio 6")
    print("Ejercicio 8")
    print("Ejercicio 10")
    while flag:
        numero = int(input("¿Qué ejercicio desea probar? (0 para salir) "))
        if numero == 0:
            flag = 0
        elif numero == 1:
            input("Imprime los primeros 20 números naturales.")
            ej1()
        elif numero == 2:
            n = int(input("Imprime la tabla de un número, ingrese el número: "))
            ej2(n)
        elif numero == 3:
            input("Imprime los números dentro del rango que elija.")
            ej3()
        elif numero == 4:
            ej4()
        elif numero == 5:
            input("Imprime los primeros 10 números de la secuencia de Fibonacci")
            ej5()
        elif numero == 6:
            ej6()
        elif numero == 8:
            ej8()
        elif numero == 10:
            ej10()
        elif numero == 11:
            ej11()
        elif numero == 12:
            ej12()
        elif numero == 13:
            ej13()
        elif numero == 14:
            ej14()
        


main()

    

