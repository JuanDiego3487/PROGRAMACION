


lstDocentes = []
totalHonorarios = 0

for i in range(1, n+1):
    print("\nDatos del docente #", i)
    datDocente = {}
    ced = input("Cedula: ")
    datDocente["ced"] = ced
    datDocente["nombre"] = input("Nombre: ") 
    datDocente["categoria"] = int(input("Categoria (1 al 5): "))
    datDocente["horas_lab"] = int(input("Horas laboradas: "))
    datDocente["honorarios"] = dicCategoria.get(datDocente["categoria"], 0) * datDocente["horas_lab"]
    
    totalHonorarios += datDocente["honorarios"]
    
    lstDocentes.append(datDocente)
    
    
print("\n\n", "=" * 30)
print("INFORME")
print("=" * 30)
print("NOMBRE\t\tHONORARIOS")
print("-" * 30)

for k, v in dicDocentes.items():
    print(f'{v["nombre"]}\t\t${v["honorarios"]:,}')

print("\n", "-" * 30)
print(f"Total honorarios: ${totalHonorarios:,}")