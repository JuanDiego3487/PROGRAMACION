def diegoElemenListPos(lst, elem):

    #FUNCION QUE BUSCA UN ELEMENTO EN LA LISTA
    #SI LO ENCUENTRA DEVUELVE LA POSICION
    #SI NO LO ENCUENTRA DEVUELVE -1

    for p in range(len(lst)):
        if elem == lst[p]:   #si element es lista en la posicion pp
            return p
        
    return -1

def existElemList(lst,elem):
    #FUNCION QUE BUSCA UN ELEMENTO EN LA LISTA
    #SI LO ENCUENTRA DEVUELVE TRUE
    #SI NO LO ENCUENTRA DEVUELVE FALSE

    for e in lst:
        if e ==elem:
            return True
    return False

