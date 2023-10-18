import json

fd = open ("/home/spukN01-010/Downloads/mbox.txt","r")
print("Digite el nombre del archivo: ")
 #fd es file description leida

lstEmails = []
for linea in fd:
    if linea.startswith("X-DSPAM-Confidence"):
        email = linea.split()[1]
        if email not in lstEmails:
            lstEmails.append(email)

for i in range(len(lstEmails)-1, -1, -1):
    # Enviar el correo
    msj = f"Average Spam confidence: {lstEmails[i]} "
    print(msj)

fd.close()

def mostrarEmails(lstEmails,):

    print("\n1. Enter the file name: mbox.txt")
    print("Avergare spam confidence", lstEmails)

    print("\n2. Enter the file name: mbox-short.txt")
    print("Avergare spam confidence", lstEmails)

    return




def menu():
    while True:
        try:
            print("*** NOMINA ACME ***".center(40))
            print("MENU".center(40))
            print("1. Mirar el nombre de archivo: ")
            print("2. Salir ")
            op = int(input(">>> Opción (1-2)? "))
            if op < 1 or op > 2:
                print("Opción no válida. Escoja de 1 a 2.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 2.")
            input("Presione cualquier tecla para continuar...")



def cargarInfo(lstEmails , ruta): 
    try: 
        fd = open(ruta, "r") 
    except Exception as e:  

        try: 
            fd = open(ruta , "w")  
        except Exception as d:  
            print("Error al intentar abrir el archivo\n" , d) 
            return None 
    try:
        linea = fd.readline()
        if linea.strip() != "": 
            fd.seek(0)
            lstEmails = json.load(fd) 
        else: 
            lstEmails = []
    except Exception as e: 
        print("Error al cargar la informacion\n" , e) 
        return None 
    
    print(lstEmails)
    fd.close() 
    return lstEmails 

## PROGRAMA PRINCIPAL 
rutaFile = "/home/spukN01-010/Downloads/mbox.txt"
lstEmails= []
lstEmails = cargarInfo(lstEmails , rutaFile)


while True:
    op = menu()
    if op == 1:
        mostrarEmails(lstEmails, rutaFile)
    elif op == 2:
        print("Haz oprimido Salir del sistema") 
        input()
        break

 

        