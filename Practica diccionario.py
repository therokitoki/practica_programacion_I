"""tambien podria tener un diccionario dentro de un diccionario, por ejemplo
d = {"Jorge" : {"Telefono: 38473", "Mail" : ueirhe@...}, "Marcos" : {"Telefono" : 34873, "Direccion": u34u34}}

Para acceder al mail de Jorge
d["Jorge"]["Telefono"]
"""

def menu():
    print("Menu de opciones: ")
    print("1- Crear nuevo contacto")
    print("2- Modificar contacto existente")
    print("3- Eliminar contacto")
    print("4- Mostrar agenda")
    print("0- Salir")
    op = int(input("Ingrese una opción (0 a 4): "))

    #Verificación
    while (op>4 or op<0):
        op = int(input("Error. Ingrese una opción (0 a 4): "))
    return op


def crearContacto(agenda: dict): #Anotacion: lo que está dsp de los 2 puntos es una explicacion para el programador de qué tipo de elemento espera
    nombre = input("Ingrese el nombre: ")
    #verificamos si existe prviamente
    if nombre in agenda:
        print("El contacto ya existe.")
    else:
        tel = input("Ingrese el teléfono: ")
        agenda[nombre] = tel
        print("El contacto fue creado con éxito.")
    

def modificarContacto(agenda: dict):
    nombre = input("Ingrese el nombre: ")
    if nombre in agenda:
        tel = input("Ingrese el teléfono: ")
        agenda[nombre] = tel
        print("El contacto fue modificado con éxito.")
    else:
        print("El contacto no existe.")

def eliminarContacto(agenda: dict):
    nombre = input("Ingrese el nombre: ")
    if nombre in agenda:
        agenda.pop(nombre) #popitem elimina la ultima que agregamos, pop elimina una especifica
        print("El contacto fue eliminado con éxito.")
    else:
        print("El contacto no existe.")

def mostrarAgenda(agenda: dict):
    for nombre, tel in agenda.items():
        print(nombre, ': ', tel)

def principal():
    agenda = {}
    opcion_ingresada = menu()

    while opcion_ingresada != 0:
        
        if opcion_ingresada == 1:
            crearContacto(agenda)
        elif opcion_ingresada == 2:
            modificarContacto(agenda)
        elif opcion_ingresada == 3:
            eliminarContacto(agenda)
        else:
            mostrarAgenda(agenda)
        print()
        opcion_ingresada = menu()
    print("¡Nos vemos!")
        

