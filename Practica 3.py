#Ejercicio 1
"""1. Dada una contraseña verificar que su longitud es superior a 8 caracteres.
"""
contraseña = input("Ingrese su contraseña: ")

if len(contraseña)>8:
  print("Contraseña aceptada. Tiene más de 8 caracteres.")
else:
  print("Su contraseña debe tener más de 8 caracteres.")

"""2. Escribir un programa que verifique si un n´umero es divisible por 4"""

numero = int(input("Ingrese su número: "))
if numero%4 == 0:
  print("El número es divisible por 4.")
else:
  print("El número no es divisible por 4.")

"""3. Determinar e informar el mayor valor de 3 números enteros. """

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

mayor = 0

if num1>=num2: 
  mayor = num1
  if num3 >=num1:
    mayor = num3
else:
  mayor = num2
  if num3 >= num2:
    mayor = num3

print("El mayor número es " + str(mayor))

"""¿Qué cambiarıas en el algoritmo si se trataran de 3 números reales o de 3 caracteres o de 3 palabras?"""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

mayor = 0

if num1>=num2: 
  mayor = num1
  if num3 >=num1:
    mayor = num3
else:
  mayor = num2
  if num3 >= num2:
    mayor = num3

print("El mayor número es " + str(mayor))

"""Dados 3 lados de un tri ́angulo, informar si el mismo es equil ́atero, is ́osceles o escaleno."""

lado1 = int(input("Ingrese el primer lado del triangulo: "))
lado2 = int(input("Ingrese el segundo lado del triangulo: "))
lado3 = int(input("Ingrese el tercer lado del triangulo: "))

if (lado1 == lado2):
  if(lado1 == lado3):
    triangulo = "Equilatero"
  else:
    triangulo = "Isosceles"
elif(lado2 == lado3):
  triangulo = "Isosceles"
else:
  triangulo = "Escaleno"

print("El triangulo es ",triangulo)

"""5. Convertir las calificaciones alfabeticas ‘I’, ‘A’, ‘B’, ‘M’, ‘D’ y ‘E’ en calificaciones num ́ericas 5, 6, 7, 8, 9 y
10 respectivamente. Ingresar una calificaci ́on alfab ́etica e informar por pantalla la calificaci ́on num ́erica
correspondiente, en caso de ingresar cualquier otra letra mostrar ((error calificaci ́on inexistente)).
"""

letra = input("Ingrese su calificación alfabética: ")
numerico = -1

while (numerico == -1):
  if letra == 'I':
    numerico = 5
  elif letra == 'A':
    numerico = 6
  elif letra == 'B':
    numerico = 7
  elif letra == 'M':
    numerico == 8
  elif letra == 'D':
    numerico == 9
  elif letra == 'E':
    numerico == 10
  else: 
    print("Error: la calificación deseada no existe.")

print("La calificación numérica es:",numero)

#Ejercicio 5
"""Convertir las calificaciones
alfabeticas ‘I’, ‘A’, ‘B’, ‘M’, ‘D’ y ‘E’
en calificaciones num ́ericas 5, 6, 7, 8, 9 y 10 respectivamente.
Ingresar una calificaci ́on alfab ́etica e informar por
pantalla la calificaci ́on num ́erica correspondiente, en caso de ingresar
cualquier otra letra mostrar ((error calificaci ́on inexistente))."""

def ej5():
    letra = input("Ingrese su calificación alfabética: ")
    letra = letra.upper()
    numerico = -1

    while (numerico == -1):
      if letra == 'I':
        numerico = 5
      elif letra == 'A':
        numerico = 6
      elif letra == 'B':
        numerico = 7
      elif letra == 'M':
        numerico = 8
      elif letra == 'D':
        numerico = 9
      elif letra == 'E':
        numerico = 10
      else: 
        print("Error: la calificación deseada no existe.")
        letra = input("Ingrese su calificación alfabética: ")

    print("La calificación numérica es:",numerico)

#Ejercicio 6
"""Escribir un programa que le pregunte a las personas su fecha de
cumplea ̃nos y en base a eso imprimir
su signo zod ́ıaco. Recomendaci ́on, pedirle a la persona ingresar la fecha con cierto formato, por ejemplo
DD/MM y si la persona no lo respeta, imprimir un mensaje de error."""

def ej6():
    fecha = input("Ingrese su fecha de cumpleaños en formato DD/MM: ")
    while(fecha[2] != '/' and len(fecha) != 5):
        print("La fecha ingresada no es válida.")
        fecha = input("Ingrese su fecha de cumpleaños en formato DD/MM: ")
    dias = int(fecha[0:2])
    mes = int(fecha[3:5])

    signos = ["Aries","Tauro","Géminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario","Capricornio","Acuario","Piscis"]

    #comenzamos a buscar los signos del zodiaco
    n = 0
    while (n != "n"):
        if mes <=6:
            if mes == 1:
                if dias > 19:
                    signo = 11
                else:
                    signo = 10
            elif mes == 2:
                if dias > 18:
                    signo = 12
                else:
                    signo = 11
            elif mes == 3:
                if dias > 20:
                    signo = 1
                else:
                    signo = 12
            elif mes == 4:
                if dias > 19:
                    signo = 2
                else:
                    signo = 1
            elif mes == 5:
                if dias > 20:
                    signo = 3
                else:
                    signo = 2
            elif mes == 6:
                if dias > 21:
                    signo = 4
                else:
                    signo = 3
        else:

            if mes == 7:
                if dias > 21:
                    signo = 5
                else:
                    signo = 4
            elif mes == 8:
                if dias > 21:
                    signo = 6
                else:
                    signo = 5
            elif mes == 9:
                if dias > 21:
                    signo = 7
                else:
                    signo = 6
            elif mes == 10:
                if dias > 21:
                    signo = 8
                else:
                    signo = 7
            elif mes == 11:
                if dias > 21:
                    signo = 9
                else:
                    signo = 8
            elif mes == 12:
                if dias > 21:
                    signo = 10
                else:
                    signo = 9

        print(signos[signo-1])

        n = input("¿Desea probar otra fecha? [y/n]")

    
