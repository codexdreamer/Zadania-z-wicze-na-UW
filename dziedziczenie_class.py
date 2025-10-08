
print("Podaj liste")
lista = input()

try:
    
    lista.reverse()
    print(lista)

except ValueError:
    print("Lista jest pusta")
    
except IndexError:
    print("Index jest pusty")
    
except TypeError:
    print("Lista nie jest listą")
    
    