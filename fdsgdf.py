def leerVH():
    while True:
        try:
            n = int(input("Por favor ingrese el valor de la hora trabajada "))
            if n < 8000 or n > 150000 or n == "":
                print("Valor de Horas trabajadas invalidas")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")


def leerHT():
    while True:
        try:
            n = int(input("Por favor ingrese el número de horas trabajadas "))
            if n < 1 or n > 160:
                print("Nunero de Horas trabajadas invalidas")
                continue
            return n
        except ValueError:
            print("Error al ingresar el número de horas trabajadas.")


def leerID():
    while True:
        try:
            n = int(input("Por favor ingrese el ID del empleado "))
            if n < 1:
                print("Nunero de la identificacion invalido")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")



def leerNombre():
    while True:
        try:
            nom = input("Por favor ingrese el nombre del empleado ")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)



def menu():
    while True:
        try:
            print("\nNOMINA ACME" )
            print("\nMENU" )
            print("1. Agregar empleado ")
            print("2. Modificar empleado ")
            print("3. Buscar empleado  ")
            print("4. Eliminar empleado  ")
            print("5. Listar empleados  ")
            print("6. Listar nómina de un empleado ")
            print("7. Listar nómina de todos los empleados  ")
            print("8. Salir ")
            op = int(input(">>> Opción (1-8)? "))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 8.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 8.")
            input("Presione cualquier tecla para continuar...")

def agregarEmpleado():
    print("\n\n1. Agregar")
    id = leerID()
    nombre = leerNombre()
    horas = leerHT()
    valor = leerVH()

    empleado = []
    empleado.append(id)
    empleado.append(nombre)
    empleado.append(horas)
    empleado.append(valor)

    lstEmpleados.append(empleado)

def obtenerEmpleado(id):
    for i in range(len(lstEmpleados)):
        if lstEmpleados[i][0] == id:
            return i
    return -1

def buscarEmpleado():
    print("\n\n3. Buscar")
    id = leerID()
    indice = obtenerEmpleado(id)
    if indice == -1:
        print("El empleado no ha sido ingresado")
    else:
        imprimirEmpleado(lstEmpleados[indice])


def imprimirEmpleado(empleado):
    print(f"id: {empleado[0]}")
    print(f"nombre: {empleado[1]}")
    print(f"horas: {empleado[2]}")
    print(f"valor: {empleado[3]}")

def modificarEmpleado():
    print("\n\n2. Modificar")   
    id = leerID()
    indice = obtenerEmpleado(id)
    if indice == -1:
        print("El empleado no existe")
    else:
        while True:
            print("\nDato a modificar" )
            print("1. Nombre ")
            print("2. Horas trabajadas ")
            print("3. Valor de la hora ")
            print("4. Volver al menu principal ")
            try:
                opcion = int(input(">>> Opción (1-4)? "))
                if opcion < 1 or opcion > 4:
                    print("Opción no válida")
                    continue
            except ValueError:
                print("Opción no válida")
            
            if opcion == 1:
                dato = leerNombre()
            elif opcion == 2:
                dato = leerHT()
            elif opcion == 3:
                dato = leerVH()
            elif opcion == 4:
                break
        
            lstEmpleados[indice][opcion] = dato

def eliminarEmpleado():
    print("\n\n4. Eliminar")   
    id = leerID()
    indice = obtenerEmpleado(id)
    if indice == -1:
        print("Empleado no encontrado, no pudo ser eliminado")
    else:
        del lstEmpleados[indice]
        print("Empleado eliminado exitosamente")

def listarEmpleados():
    print("\n\n5. Listar empleados")   
    for pag in range(0,len(lstEmpleados),5):
        for i in range(pag, min(pag+5, len(lstEmpleados))):
            print(f"Empleado en la posición {i}")
            imprimirEmpleado(lstEmpleados[i])
            print("\n")
        
        if pag + 5 < len(lstEmpleados):
            opcion = input("Desea continuar? s/n ")
            if opcion.lower() != "s":
                break
            opcion = print("\n")

#lstNombres= []
#lstIds= []
#lstHTs= []
#lstVHs= []
lstEmpleados = []

while True:
    opcion = menu()
    if opcion == 1:
        agregarEmpleado()
        print("Empleado agregado con exito:")
        input("Presione una tecla para continuar:")

        #lstNombres.append(leerNombre("Nombre? "))
        #lstIds.append(leerID("ID? "))
        #lstHTs.append(leerHT("Hora trabajada? "))
        #lstVHs.append(leerVH("Valor Hora trabajada? "))
    elif opcion == 2:
        modificarEmpleado()
        input("Presione una tecla para continuar:")
    elif opcion == 3:
        buscarEmpleado()
        input("Presione una tecla para continuar:")
    elif opcion == 4:
        eliminarEmpleado()
        input("Presione una tecla para continuar:")
    elif opcion == 5:
        listarEmpleados()
        input("Presione una tecla para continuar:")



    elif opcion == 8:
        break 