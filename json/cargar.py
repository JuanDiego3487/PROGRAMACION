import json

fd = open ( "11 archivos/lista.json","r")

lst = []

lst = json.load(fd)

for e in lst:
    print(f"Nombre:{e['nombre']}")
    print(f"Edad: {e['Edad']}")
    print("-"*30)

fd.close()
