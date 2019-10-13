def sumaLista (lista):
    if 1 == len(lista): #Verifica que la lista es de longitud uno 
        return lista[0]
    else:
        return lista[0] + sumaLista(lista[1:])
        #La funcion se llama asi mismo pero se recorre la lista. 
        
    



def main():
    print(sumaLista([3,5,2,4]))



main()
    
