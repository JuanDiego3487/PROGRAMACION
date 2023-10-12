fd = open ("11 archivos/mbox-short.txt", "r")

cl = 0
for linea in fd:
    linea= linea.strip()


cl += 1

fd.close()

print("Ejecutar",cl)