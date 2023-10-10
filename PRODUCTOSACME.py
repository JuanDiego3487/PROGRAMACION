def leerIDProduc():
    while True:
        try:
            n = int(input("Ingrese el ID del producto: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")


def leerNombreProduc():
    while True:
        try:
            nom = input("Ingrese el nombre del producto: ")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Producto inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el producto.", e)

def leerPrecioProduc():
    while True:
        try:
            n = int(input("Ingrese el precio del producto: "))
            if n < 0 :
                print("Precio no encontrado.")
                continue
            return n
        except ValueError:
            print("Error al ingresar el precio.")

def leerCantidadProduc():
    while True:
        try:
            n = int(input("Ingrese la cantidad del producto: "))
            if n < 0 :
                print("Cantidad no encontrado.")
                continue
            return n
        except ValueError:
            print("Error al ingresar el la cantidad.")

def buscarProduc(dicProduc, idProduc):
    # return dicProductos.get(idProduc) != None
    return idProduc in dicProduc
def listarEstrategiaMercadeo(dicProduc):
        for i in range (0):
            i +=1
        print(dicProduc[i])
        if i%5 ==0:
            input()
        return



def listarProducto(dicProduc):













def eliminarProducto(dicProduc):
    print("\n\n*** 3. Eliminar empleado\n")
    id = leerIDProduc()
    if buscarProduc(dicProduc, id) == False:
        print("El producto no existe en el diccionario")
        input()
    else:
        del dicProduc[id]
        print("El producto fue borrado exitosamente")
        input()
        return




def modificarProducto(dicProduc):
    print("\n\n2. Modificar Producto\n")
    
    idProduc = leerIDProduc()
    existEmpl = buscarProduc(dicProduc, idProduc)
    if existEmpl == False:
        print("El código del producto no existe.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre \n2. Precio \n3. Cantidad"))
        if op <1 or op >3:
            print("Validacion incorrecta. Presione de 1 a 3 ")
            input()
            continue
        break
    
    if op == 1:
        nombre = leerNombreProduc()
        dicProduc[idProduc]["nombre"] = nombre
    elif op == 2:
        cantProduc = leerCantidadProduc()
        dicProduc[idProduc]["Cantidad productos"] = cantProduc
        
    elif op == 3:
        valProduc = leerPrecioProduc()
        dicProduc[idProduc]["ValorProducto"] = valProduc
        
    dicProduc[idProduc]["Bodega"] = dicProduc[idProduc]["Precioproduc"] * dicProduc[idProduc]["cantidadProduc"]




def agregarProducto(dicProduc):
    print("\n\n*** 1. Agregar producto\n")
    dicDatos = {}
    id = leerIDProduc()
    if buscarProduc(dicProduc, id) == True:
        print("El id ya existe en la lista")
        input()
    
        return
    
    
    
    dicDatos["nombre"] = leerNombreProduc()
    dicDatos["HorasTrabajadas"] = leerCantidadProduc()
    dicDatos["ValorHora"] = leerPrecioProduc()
    dicDatos["Salario"] = dicDatos["ValorHora"] * dicDatos["HorasTrabajadas"]
    
    dicProduc[id] = dicDatos

def menu():
    while True:
        try:
            print("*** PRODUCTOS ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar producto")
            print("2. Modificar producto")
            print("3. Eliminar producto")
            print("4. Listar varios productos")
            print("5. Estrategia de mercadeo")
            print("6. Salir")
            op = int(input(">>> Opción (1-6)? "))
            if op < 1 or op > 6:
                print("Opción no válida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 6.")
            input("Presione cualquier tecla para continuar...")
            
## PROGRAMA PRINCIPAL
dicProduc= {}
while True:
    op = menu()
    if op == 1:
        agregarProducto(dicProduc)
        # print(dicProduc)
        # input()
    elif op == 2:
        modificarProducto(dicProduc)
        # print(dicProduc)
        # input()
    elif op == 3:
        pass
        eliminarProducto(dicProduc)
        #print(dicProduc)
        #input()
    elif op == 4:
        listarProducto(dicProduc)
        #print(dicProduc)
        #input()
    elif op == 5:
        listarEstrategiaMercadeo(dicProduc)
        #print(dicProduc)
        #input()
    elif op == 6:
        print("Gracias por usar el servicio")
        input("Presione una tecla para continuar")
