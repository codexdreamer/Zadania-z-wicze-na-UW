
while True:
    liczba = int(input("Podaj liczbę: "))
    
    if liczba % 2 == 0:
        with open('liczby_parzyste.txt', 'a') as plik:
            plik.write(str(liczba) + '\n')
    else:
        with open('liczby_nieparzyste.txt', 'a') as plik:
            plik.write(str(liczba) + '\n')
    
    wybor = input("Czy chcesz zakończyć? t=tak, inny znak - nie: ")
    if wybor.lower() == 't':
        break


with open('liczby_parzyste.txt', 'r') as plik:
    parzyste = [int(linia.strip()) for linia in plik]

with open('liczby_nieparzyste.txt', 'r') as plik:
    nieparzyste = [int(linia.strip()) for linia in plik]


suma_parzystych = sum(parzyste)
suma_nieparzystych = sum(nieparzyste)

srednia_parzystych = suma_parzystych / len(parzyste) if parzyste else 0
srednia_nieparzystych = suma_nieparzystych / len(nieparzyste) if nieparzyste else 0

print(f"Suma parzystych: {suma_parzystych}, średnia: {srednia_parzystych}")
print(f"Suma nieparzystych: {suma_nieparzystych}, średnia: {srednia_nieparzystych}")
