

def zamien_elementy(lista, i, j):
    try:
        
        if not isinstance(lista, list):
            raise TypeError("Pierwszy argument musi być listą")
        
        if not isinstance(i, int) or not isinstance(j, int):
            raise TypeError("Indeksy muszą być liczbami całkowitymi")
       
        if len(lista) == 0:
            raise ValueError("Lista jest pusta")
        
        if i >= len(lista) or j >= len(lista) or i < 0 or j < 0:
            raise IndexError("Indeksy poza zakresem listy")
        
       
        lista[i], lista[j] = lista[j], lista[i]
        print("Lista po zamianie:", lista)
        
    except (TypeError, IndexError, ValueError) as e:
        print("Błąd:", e)



    