#Escribir un programa que permita la creación 
# e introducción de los datos del libreria de 
# la empresa (Id, Nombre, Edad, Sexo y 
# Teléfono) y almacene la información de 
# forma persistente. No se pueden almacenar 
# la información de una persona varias veces, 
# deben haber registros únicos por persona.
#
# Estructura de datos elegida:
# Lista de diccionarios
# [ {id1: {nombre:"", edad: , sexo: , Telefono},
#   {id2: {nombre:"", edad: , sexo: , Telefono},
#   {idn: {nombre:"", edad: , sexo: , Telefono}
# }]


import json

def guardarLibreria(lstlibreria, ruta):
    # Función que guarda los datos de la lista de libreria
    # en un arcivo JSON
    # Devuelve True: si los datos fueron guardados correctamente
    # Devuelve False: si los datos no se pudieron guardar
    
    try:
        fd = open(ruta, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar al libreria.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        json.dump(lstlibreria, fd)
    except Exception as e:
        print("Error al guardar la información del libreria.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.")
        input("Presione cualquier tecla para continuar\n")
        return False
    
    return True

def existeId(id, lstlibreria):
    #funcion que encuentra la posición de un id en la lista
    # Devuelve un número enterior >= 0 si el id existe
    # Devuelve un -1 si el id NO existe
    for i, datos in enumerate(lstlibreria):
        # El método enumerate () agrega un contador a un iterable y 
        # lo devuelve en forma de objeto de enumeración. 
        # Este objeto enumerado puede usarse directamente para bucles 
        # o convertirse en una lista de tuplas usando la función list().
        k = int(list(datos.keys())[0])
        if k == id:
            return i
    return -1

    dsfsdf

def borrarlibreria(lstlibreria, rutaFile):
    print("\n\n3. Borrar libreria")
    
    id = int(input("Ingrese el codigo del libro: "))
    if existeId(id, lstlibreria) == -1:
        print("No existe un libro con ese codigo")
        input("Presione cualquier tecla para continuar\n")
        return None
    
    for i in range(len(lstlibreria)):   
        datos = lstlibreria[i]
        k = int(list(datos.keys())[0])
        if k == id:
            del lstlibreria[i]
            break
    
    if guardarLibreria(lstlibreria, rutaFile) == True:
        print("La libreria ha sido borrada")
        input("Presione cualquier tecla para continuar\n")
    else:
        print("Ocurrio un error al borrar la libreria")
        input("Presione cualquier tecla para continuar\n")
        return None
    
def editarLibreria(lstlibreria, rutaFile):  
    fd = open(rutaFile , "w")

    print("\n\n3. Modificar libreria") 
    codigo = int(input("Ingrese el codigo: ")) 

    if not existeId(codigo , lstlibreria): 
        print("El empleado no existe") 
        input()
        return  
    
    op = int(input("\n1. Codigo\n2. Titulo\n3. Autor \n4. Precio\nOpcion[1-4]? "))

    for i in range(len(lstlibreria)):
        datos = lstlibreria[i]
        k = int(list(datos.keys())[0])
        if k == id:
            for elemento in lstlibreria[i]:

                if op == 1: 
                    nombre = input("Ingrese el nombre correcto: ")
                    lstlibreria[i][elemento]["nombre"] = nombre 

                elif op == 2: 
                    edad = input("Ingrese la edad correcta: ")
                    lstlibreria[i][elemento]["edad"] = edad

                elif op == 3: 
                    sexo = input("Ingrese el sexo correcto: ")
                    lstlibreria[i][elemento]["sexo"] = sexo  
                
                elif op == 4: 
                    tel = input("Ingrese el teléfono correcto: ")
                    lstlibreria[i][elemento]["tel"] = tel 

            json.dump(lstlibreria, fd)
            fd.close()


def agregarLibreria(lstlibreria, ruta):
    print("\n\n1. Agregar libreria")
    
    id = int(input("Ingrese el codigo del libro: "))
    while existeId(id, lstlibreria) != -1:
        print("--> Ya existe un libreria con ese codigo")
        input("Presione cualquier tecla para continuar\n")
        id = int(input("\nIngrese el codigo del libro: "))
        

    titulo = (input("titulo: "))
    autor = input("autor: ")
    precio = float(input("Precio: "))
    
    diclibreria = {}
    diclibreria[id] = {"titulo":titulo, "autor":autor, "precio":precio}
    lstlibreria.append(diclibreria)
    
    if guardarLibreria(lstlibreria, ruta) == True:
        input("El libreria ha sido registrado con éxito.\nPresione cualquier tecla para continuar...")
    else:
        input("Ocurrio algún error al guardar el libreria.")

def menu():
    while True:
        try:
            print("\n" * 30)
            print("--- LIBRERIA---".center(40))
            print("MENU".center(40))
            print("1. codigo del libro")
            print("2. Consultar el libro ")
            print("3. Editar")
            print("4. Borrar")
            print("5. Listar")
            print("6. Salir")
            op = int(input(">>> Opción (1-6)? "))
            if op < 1 or op > 6:
                print("Opción no válida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 5.")
            input("Presione cualquier tecla para continuar...")
            
def cargarInfo(lstlibreria, ruta):
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            input("Presione cualquier tecla para continuar\n")
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstlibreria = json.load(fd)
        else:
            lstlibreria = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        input("Presione cualquier tecla para continuar\n")
        return None
    
    # print(lstlibreria)
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.\n", e, "\n")
        input("Presione cualquier tecla para continuar\n")
        return None
    return lstlibreria
    
# *** PROGRAMA PRINCIPAL ***
rutaFile = "Campus Lands\\Ciclo 1\\Grupo-C4-Sep\\Código\\11 archivos\\datlibreria.json"
lstlibreria = []
lstlibreria =cargarInfo(lstlibreria, rutaFile)
while True:
    op = menu()
    if op == 1:
        agregarLibreria(lstlibreria, rutaFile)
    elif op == 2:
        pass
    elif op == 3:
        editarLibreria(lstlibreria, rutaFile)
    elif op == 4:
        borrarlibreria(lstlibreria, rutaFile)
        pass
    elif op == 5:
        #listarlibreria(lstlibreria, rutaFile)
        pass        
    elif op == 6:
        print("\nGracias por usar el programa")
        input("Pulse cualquier tecla para volver al inicio")
        break