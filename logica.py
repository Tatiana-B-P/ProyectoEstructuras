import mook

def buscador():
    #Almacenamiento de indices y sus respectivas tutelas
    indices ={}
    #Filtro de palabras por las que se deben agrupar las tutelas
    filtro = ["violencia", "estafa", "alimentos", "salud", "pensión", "medicinas"]

    #Desglosando las tutelas que estaban en la lista mook.tutela
    for tutela in mook.tutela:
        #toma los resumenes de cada tutela y separa cada palabra del resumen en un campo de la lista resumen_tutelas
        resumen_tutela = tutela["resumen"].split()
        
        #Tomar palabra por palabra del resumen de cada tutela
        for palabra in resumen_tutela:
            #revisar si esa palabra esta en la lista de palabras filtradas
            if palabra in filtro:
                #revisar si esa palabra buscada por el usuario y filtrada previamente
                #esta en los indices(si es que los hay)
                if palabra in indices:
                    #si esa palabra ya es un indice del diccionario, adicionarle la tutela en la que se encontro esa palabra
                    indices[palabra].append(tutela)
                else:
                    #si no agregar ese indice y la tutela que tiene esa palabra en el resumen
                    indices[palabra] = [tutela]
    return indices
        
