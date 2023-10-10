milista = [] #Lista vacia
milista2 = list()

nonCampers = ["Juan", "Yulieth", "Lorenzo","Manuel","David"]
print(nonCampers)
print(nonCampers[1])
nonCampers[1] ="Julieth"
print(nonCampers[1])


#SLICES
print(nonCampers[2:4])
print(nonCampers[::-1])

nonCampersJuan = ["Daniela","Maria","Sandra","Carolina"]
print(nonCampersJuan)
#nonCampers += nonCampersJuan      #ESTE Y EL DE ABAJO LO BORRO EL PROFE
#print(nonCampers)

#Metodos de listas
nonCampers.append("Kevin")   #KEVIN SE AGREGA AL FINAL CON EL METODO APPEND
print(nonCampers)

nonCampers.extend(nonCampersJuan)   #EL ULTIMO ELEMENTO DE expend los agrega al final los elementos a la lista y append al reves
print(nonCampers)
print(nonCampers[-1])

nonCampers.insert(1, "Carlos")   #PARA AÑADIR UN DIGITO A LA DERECHA
print(nonCampers)

nonCampers.pop()        #POP ELIMINA EL ULTIMO ELEMENTO DE LA LISTA
print(nonCampers)

nonCampers.pop(-3)     #SE VA EL QUE ESTE DE ATRAS EN LA POSICION DE ATRAS
print(nonCampers)

nonCampers.remove("Juan")   
print(nonCampers)

nonCampers.sort()     #EL SORT ORDENA ALFABETICAMENTE
print(nonCampers)

nonCampers.insert(2, "Daniel")  #SE AGREGA EN LA POSICION NUMERO 2 SI ES MAYOR QUEDA ADELANNTE QUE EL OTRO
nonCampers.sort()
print(nonCampers)

#list2 = [0,1,15,"115"]
#list2.sort() v#es un error
#print(list2)

nonCampers.sort(reverse=True)
print(nonCampers)




