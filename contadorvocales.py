letras =[]
while True:
    letra = input("Ingrese una letra de abecedario: ")
    if not letra.isalpha():
        print("Error. Esa no es una letra")
        continue

    letras.append(letra)

    op = input("\nDesea continuar (S\\N)?")
    if op.lower() != "s":
            break
    
print("\n","="*30)
vocales = ["a","e","i","o","u"]
canVocales =[0]*5  #EL 0 ESTA EN LA LISTA LO MULTIPLICO POR 5 ES UYNA LISTA DE TAMAÑO 5, OSEA CREA LISTA CON 5 CEROS
#RECORRER LA LISTA POR ELEMENTOS YA QUE NO NECESITAMOS EL ORDEN
for l in letras:
     if l.lower() in vocales:     
          p = vocales.index(l.lower())
          canVocales[p] +=1

#RECORROD POR POSICION
for p in range(len(vocales)):
     print(vocales[p], "=", canVocales[p])



    