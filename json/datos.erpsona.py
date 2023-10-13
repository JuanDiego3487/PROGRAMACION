import json
#DEFINAME BORRAR PERSONAL
def borrarPersonal(lstPersonal, rutaFile):
    print("n\n3. Borrar Personal personal")

    id = int (input("Ingrese el ID: "))
    if not existeId(id, lstPersonal):
        print("No existe un empleado con ese ID")
        input()
        return
    
    for datos in lstPersonal:
        datos = lstPersonal[i]
        k = int ( list(datos.keys())[0])
        if k == id:
            del lstPersonal[i]
            break



#DEFINAME AGREGAR PERSONAL
def agregarPersonal(lstPersonal):
    print("n\n1.Agregar personal")

    id = int(input("Ingrese el ID"))
    while  existeId(id, lstPersonal):
        print("==Ya existe un empleado con ese ID")
        input()
        id= int(input("\nIngrese el ID:"))

    nombre = input("Nombre: ")
    edad = int (input("Edad: "))
    sexo = input("Sexo M/F: ")
    telefono = int (input("Telefono:"))


    dicEmpleado = []
    dicEmpleado[id] = {"nombre":nombre, "edad":edad, "sexo":sexo, "telefono":telefono}

    lstPersonal.append(dicEmpleado)

#DEFINAME ID
def existeId(id, lstPersonal):
    for datos in lstPersonal:
        k = datos.keys()[0]
        if k == id:
            return True
    return False
#DEFINAME GUARDAR EMPLEADO
def guardarEmpleado(lstPersonal,ruta):
    try:
        fd = open(ruta,"w")
    except Exception as e:
        print("Error al abrir el archivo para guardar el empleado.\n",e)
        return None
    
    try: 
        json.dump(lstPersonal, fd)
    except Exception as e: 
        print("Error al guardar la informacion del empleado.\n",e)
        return None
    

    input("El empleado ha sido registrado con exito.\nPresione cualquier tecla para continuar: ")

    if guardarEmpleado ( lstPersonal, ruta) == True:



def menu():
    while True:
        try:
            print("*** Registro del personal ***".center(40))
            print("MENU".center(40))
            print("1. Agregar ")
            print("2. Modificar")
            print("3. Eliminar ")
            print("4. Ver")
            print("5. Salir")
            op = int(input(">>> Opción (1-5)? "))
            if op < 1 or op > 5:
                print("Opción no válida. Escoja de 1 a 5.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 5.")
            input("Presione cualquier tecla para continuar...")

def cargarInfo(lstPersonal,ruta):
    try:
        fd = open(ruta,"r")
    except Exception as e:
        try:
            fd= open (ruta,"w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n" + d)
            return None
    try:
        linea = fd.readline()
        if linea.strip!= "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
        lstPersonal= json.load(fd)
    except Exception as e:
        print("Error al cargar la informacion \n", e)
        return None
    
    print()
    fd.close()
    return lstPersonal

#PROGRAMA PRINCIPAL
rutaFile = "/home/spukN01-010/campus/campus/11 archivos/datospersonal.json"
lstPersonal = []
cargarInfo(lstPersonal, rutaFile)

while True: 


    op = menu()
    if op ==1:
        agregarPersonal(lstPersonal)
    elif op ==2:
        pass
