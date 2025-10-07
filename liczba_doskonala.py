
lista_par = [
    ("Jan", "Kowalski"),
    ("Anna", "Nowak"),
    ("Piotr", "Zieliński"),
    ("Maria", "Wiśniewska"),
    ("Katarzyna", "Lewandowska"),
    ("Tomasz", "Kamiński")
]

def klucz(para):
    return para[1]


def sortowanie(lista_par):
    posortowane = sorted(lista_par,key=klucz )
    print(posortowane)
    
sortowanie(lista_par)