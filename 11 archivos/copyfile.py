fd = open ("11 archivos/nombres.txt","r")

fd2 = open                        #fd es file description

for linea in fd: 
    fd2.write(linea)

fd.close()
fd.close()

print("Proceso terminado")